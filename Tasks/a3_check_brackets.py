def check_brackets(brackets_row: str) -> bool:
    """
    Check whether input string is a valid bracket sequence
    Valid examples: "", "()", "()()(()())", invalid: "(", ")", ")("
    :param brackets_row: input string to be checked
    :return: True if valid, False otherwise
    """
    stack = []
    for bracket in brackets_row:
        if bracket == '(':
            stack.append(bracket)
        elif bracket == ')':
            if not stack:
                return False
            stack.pop()
    return False if stack else True


if __name__ == '__main__':
    print(check_brackets(""))
