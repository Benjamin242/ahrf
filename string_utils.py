'''
Pad zeros to the beginning of a number.
'''
def zero_pad(x):
    while len(x) < 3:
        x = '0' + x 
    return x

'''
Strip zeros at the beginning of a number.
'''
def strip_front_zeros(x):
    while x[0] == '0':
        x = x[1:]
    return x