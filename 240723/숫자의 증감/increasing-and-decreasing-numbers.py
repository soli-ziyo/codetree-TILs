c, n = input().split()

n = int(n)

if c =="A":
    i=1
    while i<=n:
        print(i, end=' ')
        i+=1
elif c =="D":
    i=n
    while i>=1:
        print(i, end=' ')
        i -=1