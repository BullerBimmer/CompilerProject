import unittest
from compiler.my_lexer import Lexer
from compiler.my_parser import Parser

class TestParser(unittest.TestCase):
    def test_assignment(self):        
        lexer = Lexer("x = 5")
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        result = parser.parse()
        self.assertEqual(result, [("Assignment", "x", ("NUMBER", "5"))])

    def test_print(self):
        lexer = Lexer("print 5 + 3")
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        result = parser.parse()
        self.assertEqual(result, [("Print", ("PLUS", ("NUMBER", "5"), ("NUMBER", "3")))])

    def test_use(self):
        lexer = Lexer("x")
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        result = parser.parse()
        self.assertEqual(result, [("use", "x")])

    def test_print2(self):
        lexer = Lexer("print 5")
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        result = parser.parse()
        self.assertEqual(result, [("Print", ("NUMBER", "5"))])

if __name__ == '__main__':
    unittest.main()