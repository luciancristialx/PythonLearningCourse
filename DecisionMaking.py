# 1. IF, ELSE, ELIF CLAUSE
# def checkNumbers(a, b):
#     if a == b:
#         return print("The numbers are equal.")
#     elif a > b:
#         return print("The number {0} is greater than {1}.".format(a, b))
#     elif a < b:
#         return print("The number {0} is greater than {1}.".format(b, a))
#
#
# x = input("Please enter a number for x: ")
# x = int(x)
#
# y = input("Please enter a number for y: ")
# y = int(y)
#
# checkNumbers(x, y)
#
# def checkStrings(string1: str, string2: str):
#     if string1 == string2:
#         print("The strings are equal.")
#     else:
#         print("The strings are not equal")
#
#
# c = input("Please enter a string for c variable: ")
# d = input("Please enter a string for d variable: ")
#
# checkStrings(c, d)

x = 3
y = 3
z = 2

# if x == y & x == z:
#     print('x is equal to y')
# elif x == y and x != z:
#     print('x is equal to y, but not with z.')
# else:
#     print('Nothing is matching your requirements.')

if x == y:
    if x != z:
        print("x is equal to y")
else:
    print("nothing is matching your requirements")
