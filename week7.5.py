def main():
    y = input("Insert your sentence: ")
    return count_spaces(y) # calling count_spaces function

def count_spaces(y):
    spaces = 0
    for char in y:
        if char == " ":  # if char is a space
            spaces = spaces + 1
    print("In your sentence there are",spaces, "spaces")

main()
