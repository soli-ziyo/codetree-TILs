a = int(input())

if a %2 ==0:
    b= int(a/2)
else:
    b = a

if b %2 !=0:
    c= int((b+1)/2)
    print(c)
else:
    print(b)