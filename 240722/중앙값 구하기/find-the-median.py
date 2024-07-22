a, b, c = input().split()

a = int(a)
b = int(b)
c = int(c)

if a<b and b<c:
    print(b)
elif b<c and c<a:
    print(c)
else:
    print(a)