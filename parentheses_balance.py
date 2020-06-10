"""DCS 13.5.4. Stack object is the book's example DIY stack ADT implementation,
built on a normal python list."""

from stack_additions import Stack

def balanced(string):
    """Using a stack, return True if parentheses in string are balanced, False
    if not."""
    paren_stack = Stack()
    # push each left paren onto the stack, then pop when a right is encountered.
        # if stack isn't empty at end of the function, then unbalanced.
    for char in string:
        if char == '(':
            paren_stack.push(char)
        elif char ==')':
            if paren_stack.is_empty(): # if there's a right but no lefts remaining
                                    #   to be popped, then was unbalanced
                return False
            else:
                paren_stack.pop()
    return paren_stack.is_empty()

expression = '(1+(2+3)*(4-5))'
actual = balanced(expression)
expected = True
assert actual == expected, f"actual {actual}, expected {expected}"

expression = '(1+2+3)*(4-5))'
actual = balanced(expression)
expected = False
assert actual == expected, f"actual {actual}, expected {expected}"

expression = '(1+(2+3)*(4-5)'
actual = balanced(expression)
expected = False
assert actual == expected, f"actual {actual}, expected {expected}"
