import re

NAME = "NAME"
EQ = "="
PRINT = "PRINT"
NUMBER = "NUMBER"
VARIABLE = "VARIABLE"
PLUS = "PLUS"
MINUS = "MINUS"
MUL = "MUL"
DIV = "DIV"
LPAREN = "LPAREN"
class Lexer:
    def __init__(self, source_code):
        self.source_code = source_code

    def tokenize(self):
        tokens = []
        source_code = self.source_code.split()

        for item in source_code:
            if item.isnumeric():
                tokens.append(["NUMBER", item])
            elif item in ["print"]:
                tokens.append(["PRINT"])
            elif re.match("[a-z]", item):
                tokens.append(["VARIABLE", item])
            elif item in ["+"]:
                tokens.append(["PLUS", item])
            elif item in ["-"]:
                tokens.append(["MINUS", item])
            elif item in ["*"]:
                tokens.append(["MUL", item])
            elif item in ["/"]:
                tokens.append(["DIV", item])
            elif item in ["="]:
                tokens.append(["NAME", item])
            else:
                raise ValueError(f"{item} is not a valid token.")

        return tokens
