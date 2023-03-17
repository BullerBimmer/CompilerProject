import unittest
from compiler.my_lexer import Lexer

class TestLexer(unittest.TestCase):
    def test_tokenize(self):
        # Test case 1: Simple mathematical expression
        source_code = "3 + 4 * 5"
        lexer = Lexer(source_code)
        tokens = lexer.tokenize()
        self.assertEqual(tokens, [["NUMBER", "3"], ["PLUS", "+"], ["NUMBER", "4"], ["MUL", "*"], ["NUMBER", "5"]])

        # Test case 2: Mathematical expression with variables
        source_code = "a = 3 + 4 * b"
        lexer = Lexer(source_code)
        tokens = lexer.tokenize()
        self.assertEqual(tokens, [["VARIABLE", "a"], ["NAME", "="], ["NUMBER", "3"], ["PLUS", "+"], ["NUMBER", "4"], ["MUL", "*"], ["VARIABLE", "b"]])

        # Test case 3: Invalid token
        source_code = "3 + 4 * 5 $"
        lexer = Lexer(source_code)
        with self.assertRaises(ValueError) as context:
            tokens = lexer.tokenize()
        self.assertEqual(str(context.exception), "$ is not a valid token.")

        source_code = "x = 5"
        lexer = Lexer(source_code)
        tokens = lexer.tokenize()
        self.assertEqual(tokens, [["VARIABLE", "x"], ["NAME", "="], ["NUMBER", "5"]])

        source_code = "print 5"
        lexer = Lexer(source_code)
        tokens = lexer.tokenize()
        self.assertEqual(tokens, [["PRINT"], ["NUMBER", "5"]])

if __name__ == '__main__':
    unittest.main()
