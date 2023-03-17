from compiler.my_parser import Parser
from compiler.my_lexer import Lexer
#from compiler.my_parser import Parser
#from my_lexer import NAME, EQ, NUMBER, PRINT, VARIABLE, PLUS, MINUS, MUL, DIV, LPAREN


class NumberNode:
    def __init__(self, value):
        self.value = value

class BinaryOpNode:
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right

class AssignNode:
    def __init__(self, target, value, eq):
        self.target = target
        self.value = value
        self.eq = eq

def build_ast(parse_output):
    parse_output = [parse_output]
    node_type, *args = parse_output[0]
    if node_type == 'NUMBER':
        return NumberNode(int(args[0]))
    elif node_type == 'PLUS':
        left = build_ast(args[0])
        right = build_ast(args[1])
        return BinaryOpNode('+', left, right)
    elif node_type == 'Assignment':
        target = args[0]
        value = build_ast(args[1])
        return AssignNode(target, value, '=')
    else:
        raise ValueError('Invalid node type: ' + node_type)


temp = []
def traverse(node):
    if isinstance(node, NumberNode):
        temp.append(node.value)
    elif isinstance(node, BinaryOpNode):
        traverse(node.left)
        traverse(node.right)
        temp.append(node.op)
    elif isinstance(node, AssignNode):
        temp.append(node.target)
        traverse(node.value)
        #traverse(node.eq)
    else:
        raise ValueError('Invalid node type: ' + type(node).__name__)

def tempVal():
    return temp


#lexer = Lexer("x = 5 + 3")
#tokens = lexer.tokenize()
#parser = Parser(tokens)
#parsed_tokens = parser.parse()
##transform_parsed_tokens = parsed_tokens[0]
#ast = build_ast(transform_parsed_tokens)
#test = traverse(ast)
#print(test)