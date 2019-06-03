num=int(input("Enter a Number: "))
A=[]
for i in range (1,100):
    if num%i==0:
        A.append(i)
print(A)