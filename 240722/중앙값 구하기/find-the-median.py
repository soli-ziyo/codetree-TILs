a, b, c = input().split()

a = int(a)
b = int(b)
c = int(c)

if (a<b and b<c) or (c<b and b<a):
    print(b)
elif (b<c and c<a) or (a<c and c<b):
    print(c)
else:
    print(a)