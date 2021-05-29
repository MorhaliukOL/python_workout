import random


def create_password_generator(characters):
    """
    Return function that takes one int argument 'N'
    and returns characters with 'N' random characters from 'characters'
    """

    def password_generator(length):
        
        return ''.join([random.choice(characters) for _ in range(length)])

    return password_generator



if __name__ == '__main__':
    characters = input('Enter sequence from which password will be generated:\n')
    N = int(input('Enter password length:\n'))

    n_password_generator = create_password_generator(characters)
    print(n_password_generator(N))
