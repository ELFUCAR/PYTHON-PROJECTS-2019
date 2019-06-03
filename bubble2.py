a=[1,10,2,4]

def bubble(a,c):
    d=len(a)
    for j in range (d-2):
        for i in range (d-1):
            if c =='a':
                if a[i]> a[i+1]:
                    t=a[i+1]
                    a[i+1]=a[i]
                    a[i]=t

            if c == 'd':
                if a[i] < a[i + 1]:
                     t = a[i + 1]
                     a[i + 1] = a[i]
                     a[i] = t

    return (a)


print (bubble(a,'a'))
print (bubble(a,'d'))
