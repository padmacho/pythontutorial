''' A module for demonstrating raise '''
import sys

def convert(s):
    ''' convert string to an integer '''
    try:
        return int(s)
    except (ValueError, TypeError) as e:
        print("Conversion error:{}".format(str(e)), file=sys.stderr)
        raise

if __name__ == "__main__":
    print("Convert String to int", convert("1,234"))
