

def convert_input(uinput: str, dtype: str='int', empty: bool=False):
    """
    Return user input (uinput) converted to 'dtype'
    if possible, else ask for valid input
    """
    
    dtypes = {
            'int': int,
            'float': float
            }
    assert dtype in dtypes

    try:
        converted = dtypes[dtype](uinput)
        return converted
    except ValueError:
        if empty and not uinput:
            return False

        print(f'\nInvalid input type, recieved - {type(uinput)};\nexpected - {dtype}\n')

