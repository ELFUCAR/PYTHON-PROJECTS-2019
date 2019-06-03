import random
x=int (random.randint(1, 10))
a=int(input("enter a number "))

if x==a:
    print("x:",x,",guess:",a,"your guess is exactly right")
elif x<a:
    print("x:",x,",guess:",a,"your guess is to high")
elif x>a:
    print("x:",x,",guess:",a,"your guess is to low")