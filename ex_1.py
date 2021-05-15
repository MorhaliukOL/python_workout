import random


def get_int_input() -> int:
    """
    Take input from user and convert it to integer.
    If user input cannot be converted to int, ask user to try again
    """

    # Fix 'int  '-like inputs (with trailing spaces) !!!

    num_str = input('>')
    try:
        num = int(num_str)
        return num
    except ValueError:
        print(f'Please enter number, not {num_str}.')
        get_int_input()


def guessing_game():
    """
    Ask user to guess random number from 0 to 100
    """

    number = random.randint(0, 100)
    print('Enter number from 0 to 100 (inclusive)')


    while True:
        guess = get_int_input()

        if guess == number:
            print(f'Congratulation your guess is correct -- {number}')
            input()
            break

        elif guess < number:
            print('Too low')
        else:
            print('Too high')


if __name__ == '__main__':
    guessing_game()
