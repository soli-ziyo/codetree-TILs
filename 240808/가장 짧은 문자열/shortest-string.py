a= input() ; b = input() ; c = input()
a = len(a) ; b = len(b) ; c = len(c)
if a >=b and a>=c:
    max_len = a
elif b>=c and b>=a:
    max_len = b
else:
    max_len = c 

if a <=b and a <=c:
    min_len= a
elif b<=c and b<=a:
    min_len = b
else:
    min_len = c

print(max_len - min_len )