a, b= map(int, input().split())
cnt =0
final= 0
for i in range(a, b+1):
    for j in range(1, i+1):
        if i %j==0:
            cnt +=1
    if cnt ==3:
        final +=1
    cnt =0
print(final)