''' A module for demonstrating exceptions '''
def convert(s):
    ''' convert string to an integer '''
    x = -1
    try:
        x = int(s)
    except (ValueError, TypeError):
        pass
    return x

if __name__ == "__main__":
    print("Convert String to int", convert([1, 2, 3, 4]))
