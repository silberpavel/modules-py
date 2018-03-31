

def hello():
    return 'Hi there '

def decor(fn):
    return lambda: '_' + fn() + '_'

hello = decor(hello)