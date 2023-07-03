# Concepts:
# 1. for
# 2. while
# 3. DO-while
# 4. break
# 5. continue

# FOR
# I
# x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# y = ["red", "green", "blue", "yellow", "black"]
#
# for item in x:
#     print(item + 10)
#
# for color in y:
#     print(color)
# II
# x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# for i in x:
#     x[i] = input("Enter your name: ")
# print(x)

# WHILE
# i = 0
# while i < 6:
#     print(i)
#     i += 1

# Loop through string value
# x="blueberry"
#
# for i in x:
#     print(i)

# BREAK
# y = ["red", "green", "blue", "yellow", "black"]
# for i in y:
#     if i == "yellow":
#         break
#     print(i)

# Continue
# y = ["red", "green", "blue", "yellow", "black"]
# for i in y:
#     if i == "yellow":
#         continue
#     print(i)

# RANGE Function
# .range(startingPoint, endPoint, order)
# for x in range(10):
#     print(x)

# ELSE in FOR Loop
# for x in range(10):
#     print(x)
# else:
#     print("Now the seats are full or it's over")

# NESTED Loops
x = ["big", "small", "bold", "light", "heavy"]
y = ["iron", "silver", "gold", "platinum", "diamond"]
a = 0
b = 0

for i in x:
    for j in y:
        print(x[a], y[b])
        b += 1
    a += 1
    b = 0
