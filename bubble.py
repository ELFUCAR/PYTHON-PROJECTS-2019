a=[1,10,2,4]

d=len(a)
for j in range (d-2):
    for i in range (d-1):
        if a[i]> a[i+1]:
            t=a[i+1]
            a[i+1]=a[i]
            a[i]=t


print (a) #liste halinde yazdırır
for i in range(d):
    print(a[i])
