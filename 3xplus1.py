x = int(input("Give a value for x:"))
while x > 1:
    if (x % 2) == 0:
        x = x /2
        print(x)
    else:
        x = x * 3 + 1
        print(x)

