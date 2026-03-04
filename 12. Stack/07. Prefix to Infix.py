"""
You are given a string s representing a prefix expression. Convert this prefix expression to an infix expression.

Prefix expression: The expression of the form op a b. When an operator is followed by two operands.
Infix expression: The expression of the form a op b. When an operator is in between every pair of operands.
"""

def prefix_to_infix(expression):
    stack = []
    # Reverse the prefix expression to process from right to left
    for char in reversed(expression):
        if char.isalnum():  # If the character is an operand (number or variable)
            stack.append(char)
        else:  # The character is an operator
            operand1 = stack.pop()
            operand2 = stack.pop()
            new_expr = f'({operand1} {char} {operand2})'
            stack.append(new_expr)

    return stack[-1]  # The final infix expression will be at the top of the stack
test_expression = "*+AB-CD"
print("Prefix Expression: ", test_expression)
print("Infix Expression: ", prefix_to_infix(test_expression))