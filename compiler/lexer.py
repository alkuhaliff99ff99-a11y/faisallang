from enum import Enum


class TokenType(Enum):
    LET = "LET"
    PRINT = "PRINT"

    IDENTIFIER = "IDENTIFIER"

    NUMBER = "NUMBER"

    STRING = "STRING"

    EQUAL = "="

    EOF = "EOF"


class Token:

    def __init__(self, token_type, value):
        self.type = token_type
        self.value = value

    def __repr__(self):
        return f"{self.type}:{self.value}"


class Lexer:

    def __init__(self, text):
        self.text = text

    def tokenize(self):

        tokens = []

        lines = self.text.split()

        for word in lines:

            if word == "دع":
                tokens.append(Token(TokenType.LET, word))

            elif word == "اطبع":
                tokens.append(Token(TokenType.PRINT, word))

            elif word == "=":
                tokens.append(Token(TokenType.EQUAL, word))

            elif word.isdigit():
                tokens.append(Token(TokenType.NUMBER, int(word)))

            else:
                tokens.append(Token(TokenType.IDENTIFIER, word))

        tokens.append(Token(TokenType.EOF, None))

        return tokens
