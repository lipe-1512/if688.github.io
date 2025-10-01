from enum import Enum

class TokenType(Enum):
    # Marcadores
    EOF = -1
    ILLEGAL = -2
    # Identificadores e Literais
    ID = 1
    INTEGER = 2
    # Operadores
    ASSIGN = 3 # =
    PLUS = 4 # +
    MINUS = 5 # -
    BANG = 6 # !
    ASTERISK = 7 # *
    LT = 8 # <
    GT = 9 # >
    EQ = 10 # ==
    NOT_EQ = 11 # !=
    LTE = 12 # <=
    GTE = 13 # >=
    AND = 14 # &&
    # Delimitadores
    COMMA = 15 # ,
    SEMICOLON = 16 # ;
    DOT = 17 # .
    LPAREN = 18 # (
    RPAREN = 19 # )
    LBRACE = 20 # {
    RBRACE = 21 # }
    LBRACKET = 22 # [
    RBRACKET = 23 # ]
    # Palavras-chave
    BOOLEAN = 24
    CLASS = 25
    PUBLIC = 26
    EXTENDS = 27
    STATIC = 28
    VOID = 29
    MAIN = 30
    STRING = 31
    INT = 32
    WHILE = 33
    FOR = 34
    IF = 35
    ELSE = 36
    RETURN = 37
    LENGTH = 38
    TRUE = 39
    FALSE = 40
    THIS = 41
    NEW = 42
    SOUT = 43 
    BREAK = 44

class Token:
    def __init__(self, token_type, literal):
        self.token_type = token_type
        self.literal = literal