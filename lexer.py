import re

class Lexer:
    def __init__(self, source_code):
        self.source_code = source_code

    def tokenize(self):
        tokens = []
        source_code = self.source_code.split()

        for item in source_code:
            if item.isnumeric():
                tokens.append(["NUMBER", item])
            elif re.match("[a-z]", item):
                tokens.append(["VARIABLE", item])
            elif item in ["+", "-", "*", "/"]:
                tokens.append(["OPERATOR", item])
            else:
                raise ValueError(f"{item} is not a valid token.")

        return tokens
