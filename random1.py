import random
avg=0
sum=0
n=1000
for x in range(n):
    x=int(random.random()*6)+1
    sum=sum+x
   # print(x)
avg=sum/n


print (avg)
