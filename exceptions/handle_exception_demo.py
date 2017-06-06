''' A module for demonstrating exceptions '''
def convert(s):
    ''' convert string to an integer '''
    try:
         x = int(s)
         print("Conversion is successful!")
    except ValueError:
        x = -1
        print("Conversion is failed!")
    return x

if __name__ == "__main__":
    print("Convert String to int", convert("10"))
    print("Convert String to int", convert("Hello world"))
