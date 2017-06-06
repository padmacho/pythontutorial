''' A module for demonstrating raise '''
import sys

def div(x, y):
    ''' convert string to an integer '''
    if y == 0:
        raise ValueError("y cannot be zero {}".format(y))
    return x / y
     
if __name__ == "__main__":
    print("Division div(10,5) ", div(10, 5))
    print("Division div(10,0)", div(10, 0))
