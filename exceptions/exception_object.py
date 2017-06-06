''' A module for demonstrating exceptions '''
import sys

def convert(s):
    ''' convert string to an integer '''
    x = -1
    try:
        x = int(s)
    except (ValueError, TypeError) as e:
        print("Conversion error:{}".format(str(e)), file=sys.stderr)
    return x

if __name__ == "__main__":
    print("Convert String to int", convert([1, 2, 3, 4]))