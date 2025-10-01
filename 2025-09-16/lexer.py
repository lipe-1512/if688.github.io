import sys
from tokens import Token, TokenType

class Lexer:
    def __init__(self, source):
        self.source = source
        self.curPos = 0
        self.curChar = self.source[self.curPos] if self.source else '\0'

    def nextChar(self):
        self.curPos += 1
        if self.curPos >= len(self.source):
            self.curChar = '\0'
        else:
            self.curChar = self.source[self.curPos]

    def peek(self):
        if self.curPos + 1 >= len(self.source):
            return '\0'
        return self.source[self.curPos + 1]

    def abort(self, message):
        sys.exit("Erro Léxico. " + message)

    def skipWhitespace(self):
        while self.curChar in [' ', '\t', '\r', '\n', '\f']:
            self.nextChar()

    def skipComment(self):
        # Comentário de linha //
        if self.curChar == '/' and self.peek() == '/':
            while self.curChar != '\n' and self.curChar != '\0':
                self.nextChar()
            self.nextChar()
        # Comentário de múltiplas linhas /* */
        elif self.curChar == '/' and self.peek() == '*':
            self.nextChar()  # consume '/'
            self.nextChar()  # consume '*'
            while True:
                if self.curChar == '\0':
                    self.abort("Comentário não fechado")
                if self.curChar == '*' and self.peek() == '/':
                    self.nextChar()
                    self.nextChar()
                    break
                else:
                    self.nextChar()

    def getToken(self):
        while True:
            self.skipWhitespace()
            if self.curChar == '/':
                if self.peek() == '/' or self.peek() == '*':
                    self.skipComment()
                    continue
                else:
                    break
            # Verifica se é System.out.println antes de qualquer outra coisa
            if self.source[self.curPos:self.curPos+17] == "System.out.println":
                self.curPos += 17
                if self.curPos >= len(self.source):
                    self.curChar = '\0'
                else:
                    self.curChar = self.source[self.curPos]
                return Token(TokenType.SOUT, "System.out.println")

        if self.curChar == '\0':
            return Token(TokenType.EOF, "")

        # Palavras reservadas e identificadores
        if self.curChar.isalpha() or self.curChar == '_':
            startPos = self.curPos
            while self.curChar.isalnum() or self.curChar == '_':
                self.nextChar()
            text = self.source[startPos:self.curPos]
            keywords = {
                "boolean": TokenType.BOOLEAN,
                "class": TokenType.CLASS,
                "public": TokenType.PUBLIC,
                "extends": TokenType.EXTENDS,
                "static": TokenType.STATIC,
                "void": TokenType.VOID,
                "main": TokenType.MAIN,
                "String": TokenType.STRING,
                "int": TokenType.INT,
                "while": TokenType.WHILE,
                "for": TokenType.FOR,
                "if": TokenType.IF,
                "else": TokenType.ELSE,
                "return": TokenType.RETURN,
                "length": TokenType.LENGTH,
                "true": TokenType.TRUE,
                "false": TokenType.FALSE,
                "this": TokenType.THIS,
                "new": TokenType.NEW,
                "break": TokenType.BREAK
            }
            token_type = keywords.get(text, TokenType.ID)
            return Token(token_type, text)

        # Literais inteiros
        if self.curChar.isdigit():
            startPos = self.curPos
            while self.curChar.isdigit():
                self.nextChar()
            text = self.source[startPos:self.curPos]
            return Token(TokenType.INTEGER, text)

        # Operadores e delimitadores
        # Dois caracteres
        two_char_ops = {
            "&&": TokenType.AND,
            "<=": TokenType.LTE,
            ">=": TokenType.GTE,
            "==": TokenType.EQ,
            "!=": TokenType.NOT_EQ
        }
        ch = self.curChar
        ch2 = ch + self.peek()
        if ch2 in two_char_ops:
            self.nextChar()
            self.nextChar()
            return Token(two_char_ops[ch2], ch2)

        # Um caractere
        one_char_ops = {
            '=': TokenType.ASSIGN,
            '+': TokenType.PLUS,
            '-': TokenType.MINUS,
            '!': TokenType.BANG,
            '*': TokenType.ASTERISK,
            '<': TokenType.LT,
            '>': TokenType.GT,
            ',': TokenType.COMMA,
            ';': TokenType.SEMICOLON,
            '.': TokenType.DOT,
            '(': TokenType.LPAREN,
            ')': TokenType.RPAREN,
            '{': TokenType.LBRACE,
            '}': TokenType.RBRACE,
            '[': TokenType.LBRACKET,
            ']': TokenType.RBRACKET
        }
        if ch in one_char_ops:
            self.nextChar()
            return Token(one_char_ops[ch], ch)

        self.abort(f"Caractere desconhecido: {self.curChar}")
