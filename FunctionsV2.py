def temp(c):
    f = (9 / 5) * c + 32
    return print(f)


c = input("Write the temperature in celsius: ")
c = int(c)
temp(c)


def len(minutes, seconds):
    hour = minutes / 60 + seconds / 3600
    return print(hour)


m = input("Write the numbers of minutes: ")
m = int(m)
s = input("Write the numbers of seconds: ")
s = int(s)
len(m, s)
