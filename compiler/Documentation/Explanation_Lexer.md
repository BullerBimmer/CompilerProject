The lexer (tokenizer) is the first part of a compiler. It takes the input source code and turns it into a stream of tokens. That can then be easily parsed by the compiler.

The current simple lexer defines a lexer class that takes in source code as a string in the constructor. It then has a method that tokenizes the source code and returns a list of tokens.

Technically the token methods does the following:
1. Initializes an empty list called tokens.
2. Splits the source code into a list of individual words, using .split() method.
3. Iterates through each word in the source code.
4. Checks whether the current word is a number using isnumeric() method, if it is, it appends a tuple of the form ["NUMBER", word] to the tokens list.
5. If it's not a number, it checks whether the current word is a variable using regular expression match re.match("[a-z]", item), if it is, it appends a tuple of the form ["VARIABLE", word] to the tokens list.
6. If it's not a variable, it checks whether the current word is an operator +, -, *, /, if it is, it appends a tuple of the form ["OPERATOR", word] to the tokens list.
6. If the current word does not match any of the above conditions, it raises a ValueError with a message indicating that the word is not a valid token.
7. Finally, it returns the tokens list as the result of the tokenize method.

