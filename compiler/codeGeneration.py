from my_lexer import Lexer
from my_parser import Parser

def push_eax():
    print("push eax")


def generate_code(node):

    if isinstance(node, Assignment):
        # Generate code for the right-hand side expression
        generate_code(node.value)

        # Store the result in the variable
        print(f"mov DWORD [{node.variable.name}], eax")

    elif isinstance(node, _parser.factor):
        # Generate code for the left-hand and right-hand sides
        generate_code(node.left)
        push_eax()
        generate_code(node.right)

        # Pop the left-hand side from the stack and perform the operation
        print("pop ebx")
        print("add eax, ebx" if node.op == "+" else "imul eax, ebx")

    elif isinstance(node, _parser.number):
        # Load the value into the EAX register
        print(f"mov eax, {node.value}")

    elif isinstance(node, _parser.SimpleVar):
        # Load the value of the variable into the EAX register
        print(f"mov eax, DWORD [{node.name}]")



# Define the input program
#program = "x = 2 + 3 * 4"
#program = "x = 3 + 5 - 3"
# Create a lexer and parser
##_lexer = Lexer(program)
#_lexer = _lexer.tokenize()
#_parser = Parser(_lexer)

# Parse the input program and generate code
#ast = _parser.parse()
#print(ast)
#print(ast[0])
#generate_code(ast)

