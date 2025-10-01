import sys
from lexer import *

def main():
    if len(sys.argv) != 2:
        sys.exit("Erro: Precisamos de um arquivo como argumento.")
    with open(sys.argv[1], 'r') as inputFile:
        input = inputFile.read()
        
    lexer = Lexer(input)
    print(input)
    token = lexer.getToken()
    while token.token_type != TokenType.EOF:
        print(f"Tipo: {token.token_type.name.ljust(15)} | Texto: '{token.literal}'")
        token = lexer.getToken()

main()