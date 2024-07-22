a, b, c = input().split()
a, b, c = int(a), int(b), int(c)

if a>=b and a>=c:
    print(a)
elif b>=c and b>=a:
    print(b)
else:
    print(c)