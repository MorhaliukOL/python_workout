

def mysum(*numbers):
    """
    Return sum of all int or float type arguments 
    and count of other type arguments
    
    >>> mysum(1, 2, 3)
    (6, 0)
    >>> mysum(3, 1.5, 0.3, 4.2, 'string', None)
    (9.0, 2)
    >>> mysum(1, True, '5')
    (2, 1)
    """
    if not numbers:
        raise TypeError('mysum() takes at least one positional argument (0 given)')

    total = 0
    other = 0

    for number in numbers:
        if isinstance(number, int) or isinstance(number, float):
            total += number
        else:
            other += 1

    return total, other



if __name__ == "__main__":
    import doctest
    doctest.testmod()
