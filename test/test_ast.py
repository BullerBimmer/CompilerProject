import unittest
from compiler.my_lexer import Lexer
from compiler.my_parser import Parser
from compiler.ast import BinaryOpNode, NumberNode, AssignNode, build_ast, traverse, tempVal

class TestAst(unittest.TestCase):
    def test_ast(self):        
        lexer = Lexer("x = 5 + 3")
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        parsed_tokens = parser.parse()
        _ast = parsed_tokens[0]
        _ast = build_ast(_ast)

        temp = traverse(_ast)
        _temp = tempVal()
        
        self.assertEqual(_temp, ['x', 5, 3, '+'])

