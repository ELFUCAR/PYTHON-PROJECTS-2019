def palindrome(s):
    d=len(s)
    for i in range (d//2):
        if s[i]!=s[d-1-i]:
            return False

    return True

s=input("enter a string: ")
if palindrome(s)==True:
    print(s + " is a palindrome")
else:
    print(s + " is not a palindrome")


'''
s='ala'
print(s,palindrome(s))

s='1222'
print(s,palindrome(s))

s='oojo'
print(s,palindrome(s))

s='o'
print(s,palindrome(s))
'''