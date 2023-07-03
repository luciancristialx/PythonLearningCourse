# Methods
# r, r+(read + write)
# w, w+(read + write)
# a, a+(read + append)
# x - create file

# Open & read file
# file = open("test.txt", "r")
# x = file.read()
# print(x)
# file.close()

# Open & write file (file content gets overwritten)
# file2 = open("test2.txt", "w")
# file2.write("pink")
# file2.close()

# x = ["a", "b", "c"]
# file = open("test.txt", "w")
# for letter in x:
#     file.write(letter + "\n")
# file.close()

# Open & append data
# file = open("test.txt", "a")
# file.write("purple\n")
# file.close()
