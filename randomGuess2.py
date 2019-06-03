import random
x=random.random()
x=(int)(100*x)+1
ans=0

while (ans!=x):
    ans=input("give a number")
    ans=int(ans)
    if ans<x:
        print ("too small")
    else:
        print ("too big")

print ("you guessed the number. my number was",x)