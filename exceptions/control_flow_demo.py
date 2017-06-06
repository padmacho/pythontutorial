''' A module for demonstrating exceptions '''
def convert(s):
    ''' convert string to an integer '''
    x = int(s)
    return x

if __name__ == "__main__":
    print("Convert String to int", convert("10"))
    # This will cause exception
    print("Convert String to int", convert("Hello world"))
