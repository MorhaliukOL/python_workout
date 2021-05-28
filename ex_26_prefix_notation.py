import operator

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '%': operator.mod,
    '//': operator.floordiv,
    '**': operator.pow
}

def calc(expression):
    """
    Return result of a given 'expression'.
    Expected expression format:
        operator argument1 argument2

    Example:
    >>> + 4 8
    12.0
    """
    operator, arg1, arg2 = expression.split()
    arg1, arg2 = float(arg1), float(arg2)
    return operators[operator](arg1, arg2)



if __name__ == '__main__':
    expression = input("Enter expression in prefix notation, with 2 arguments\n")
    print(calc(expression))
