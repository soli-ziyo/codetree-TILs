a, b, c = map(int, input().split())
yn =True

for i in range(a, b+1):
    if i %c ==0:
        yn =True
        break
    else:
        yn = False

if yn ==False:
    print("YES")
else:
    print("NO")