
def sum_numbers():
    """
    Ask user to enter space seperated sequence of integers
    and return their sum ignoring all inputs 
    that are not integers.
    """
    nums_string = input('Enter integer numers with spaces between them:\n')

    # here `sum` takes generator expression instead of list comprehension
    # in order to use less memory
    return sum(int(num) 
            for num in nums_string.split() 
            if num.isdigit())


if __name__ == '__main__':
    print(sum_numbers())
