import random
total=0
n=100
result=[0,0,0,0,0,0,0,0,0,0,0]

r_2=0
r_3=0
r_4=0
r_5=0


for i in range(n):
    x=int(random.random()*6)+1
    y = int(random.random() * 6) + 1

    place=x+y-2
    result[place]+= 1

for i in range(n):
    print(i+2,result[i])