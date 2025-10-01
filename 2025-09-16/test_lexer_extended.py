import unittest
from lexer import Lexer
from tokens import TokenType

class TestLexerExtended(unittest.TestCase):
    def test_comments(self):
        source = """
        // comentário de linha
        int x = 10; /* comentário
        de múltiplas linhas */
        """
        lexer = Lexer(source)
        tokens = []
        token = lexer.getToken()
        while True:
            tokens.append(token.token_type)
            if token.token_type == TokenType.EOF:
                break
            token = lexer.getToken()
        # Deve conter tokens para int, id, assign, integer, semicolon e EOF
        self.assertIn(TokenType.INT, tokens)
        self.assertIn(TokenType.ID, tokens)
        self.assertIn(TokenType.ASSIGN, tokens)
        self.assertIn(TokenType.INTEGER, tokens)
        self.assertIn(TokenType.SEMICOLON, tokens)
        self.assertIn(TokenType.EOF, tokens)

    def test_two_char_operators(self):
        source = "a && b <= c >= d == e != f"
        lexer = Lexer(source)
        expected_tokens = [
            TokenType.ID, TokenType.AND, TokenType.ID, TokenType.LTE,
            TokenType.ID, TokenType.GTE, TokenType.ID, TokenType.EQ,
            TokenType.ID, TokenType.NOT_EQ, TokenType.ID
        ]
        tokens = []
        token = lexer.getToken()
        while token.token_type != TokenType.EOF:
            tokens.append(token.token_type)
            token = lexer.getToken()
        self.assertEqual(tokens, expected_tokens)

    def test_unknown_character(self):
        source = "@"
        lexer = Lexer(source)
        with self.assertRaises(SystemExit):
            lexer.getToken()

    def test_varied_input(self):
        source = """
        class Test {
            public static void main(String[] args) {
                int x = 0;
                while (x < 10) {
                    System.out.println(x);
                    x = x + 1;
                }
            }
        }
        """
        lexer = Lexer(source)
        tokens = []
        token = lexer.getToken()
        while token.token_type != TokenType.EOF:
            tokens.append(token.token_type)
            token = lexer.getToken()
        # Verifica se alguns tokens importantes estão presentes
        self.assertIn(TokenType.CLASS, tokens)
        self.assertIn(TokenType.PUBLIC, tokens)
        self.assertIn(TokenType.STATIC, tokens)
        self.assertIn(TokenType.VOID, tokens)
        self.assertIn(TokenType.MAIN, tokens)
        self.assertIn(TokenType.INT, tokens)
        self.assertIn(TokenType.WHILE, tokens)
        self.assertIn(TokenType.SOUT, tokens)
        self.assertIn(TokenType.EOF, tokens)

if __name__ == "__main__":
    unittest.main()
