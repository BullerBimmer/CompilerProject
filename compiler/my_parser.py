from compiler.my_lexer import NAME, EQ, NUMBER, PRINT, VARIABLE, PLUS, MINUS, MUL, DIV, LPAREN
from compiler.my_lexer import Lexer

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.index = 0

    def parse(self):
        statements = []
        while self.index < len(self.tokens):
            if self.tokens[self.index][0] == NAME:
                statements.append(self.assignment())
            elif self.tokens[self.index][0] == PRINT:
                statements.append(self.print_statement())
            elif self.tokens[self.index][0] == VARIABLE and len(self.tokens) == 1:
                statements.append(self.simpleVar())
            elif self.index == len(self.tokens)-1:
                raise Exception("Invalid statement")
            self.index += 1
        return statements

    def assignment(self):
        name = self.tokens[self.index-1][1]
        self.index += 1
        #if self.tokens[self.index][0] != EQ:
        #    raise Exception("Invalid assignment")
        #self.index += 1
        value = self.expression()
        return ("Assignment", name, value)

    def print_statement(self):
        self.index += 1
        value = self.expression()
        return ("Print", value)

    def simpleVar(self):
        var = self.tokens[self.index][1]
        self.index += 1
        return ("use", var)

    def expression(self):
        left = self.term()
        while self.index < len(self.tokens) and self.tokens[self.index][0] in (PLUS, MINUS):
            op = self.tokens[self.index][0]
            self.index += 1
            right = self.term()
            left = (op, left, right)
        return left

    def term(self):
        left = self.factor()
        while self.index < len(self.tokens) and self.tokens[self.index][0] in (MUL, DIV):
            op = self.tokens[self.index][0]
            self.index += 1
            right = self.factor()
            left = (op, left, right)
        return left

    def factor(self):
        token = self.tokens[self.index]
        if token[0] in (PLUS, MINUS):
            self.index += 1
            return (token[0], self.factor())
        elif token[0] == NUMBER:
            self.index += 1
            return ("NUMBER", token[1])
        elif token[0] == LPAREN:
            self.index += 1
            result = self.expression()
            self.index += 1
            return result
        elif token[0] == NAME:
            self.index += 1
            return ("NAME", token[1])
        else:
            raise Exception("Invalid factor")
