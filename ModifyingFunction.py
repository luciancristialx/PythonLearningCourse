def div(a, b):
    if b == 0:
        return print("This is not possible!")
    else:
        c = a / b
        return print(c)


x = input("Please enter any value: ")
y = input("Please enter the second value: ")
div(int(x), int(y))
