def main():
    while True:
        a = int(input("Enter a number to find even or odd or press ctrl c to exit "))
        b = a % 2
        if b > 0:
            print("The number is odd")
        else:
            print("The number is even")

# Calling the main function
main()