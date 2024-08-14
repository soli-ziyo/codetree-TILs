import sys
def min_num(a,b,c):
    minnum = sys.maxsize
    if a <=b and a<=c:
        minnum = a 
    elif b <=a and b<=c:
        minnum = b
    else:
        minnum = c
    return minnum

a,b,c = map(int, input().split())
print(min_num(a,b,c))