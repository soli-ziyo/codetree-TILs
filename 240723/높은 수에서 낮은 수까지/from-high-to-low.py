a, b = map(int, input().split())

if a>b:
    i=a
    while i>=b:
        print(i, end=' ')
        i -=1
else:
    i=b
    while i>=a:
        print(i, end=' ')
        i -=1