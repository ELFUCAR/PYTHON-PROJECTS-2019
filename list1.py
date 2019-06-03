
A=[2,5,6,6,7,8,8,8,9]
B=[2,6,6,8,8]
C=[]
for x in A:
     if x not in C and x in B:
        C.append(x)
print(C," is in A and B")


