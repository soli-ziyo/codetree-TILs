a = int(input())

if a %2 !=0:
    b=a+3
else:
    b=a

if b %3 ==0:
    b = b//3
    print(b)