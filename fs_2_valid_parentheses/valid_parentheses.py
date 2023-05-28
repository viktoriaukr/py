def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """

    correct = []
    opening = '('
    closing = ')'
    for i in parens:
        if i in opening:
            correct.append(i)
        elif i in closing:
            if not correct:
                return False
            if opening.index(correct.pop()) != closing.index(i):
                return False
    return len(correct) == 0
