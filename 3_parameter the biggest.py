a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

def max_3(a,b,c):


    if (a >= b) and (a >= c):
        big =a
    elif (b>= a) and (b >= c):
        big = b
    else:
        big = c

    return (big)


print(a, ",", b, "and", c, "the biggest number:",max_3(a,b,c))




