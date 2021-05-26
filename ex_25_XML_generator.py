
def myxml(tag, text='', **kwargs):
    """
    Return given 'text' wrapped in xml 'tag'
    with attributes from 'kwargs' if given.
    """
    attrs = ''.join([f' {key}="{val}"' for key, val in kwargs.items()])
    return f"<{tag}{attrs}>{text}</{tag}>"



if __name__ == '__main__':
    print(myxml('foo'))
    print(myxml('foo', 'bar'))
    print(myxml('foo', 'bar', a=1, b=2, c=3))

