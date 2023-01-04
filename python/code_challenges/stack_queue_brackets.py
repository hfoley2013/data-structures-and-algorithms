# Check that all brackets have corresponding closing bracket
def multi_bracket_validation(code):
    stack = []
    for char in code:
        if char in ('(', '{', '['):
            stack.append(char)
        elif char in (')', '}', ']'):
            if not stack:
                return False
            if char == ')' and stack[-1] == '(':
                stack.pop()
            elif char == '}' and stack[-1] == '{':
                stack.pop()
            elif char == ']' and stack[-1] == '[':
                stack.pop()
            else:
                return False
    return not stack

if __name__ == '__main__':
    code = "(var x = {y: [1, 2, 3]});"
    print(multi_bracket_validation(code))  # Output: True

    code = "(var x = {y: [1, 2, 3]});"
    print(multi_bracket_validation(code))  # Output: True

    code = "(var x = {y: [1, 2, 3]}"
    print(multi_bracket_validation(code))  # Output: False
