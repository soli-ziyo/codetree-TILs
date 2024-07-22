sum=0
cnt=0
for i in range(10):
    n= int(input())
    if 0<=n and n<=200:
        cnt +=1
        sum +=n
print(f"{sum} {sum/cnt:.1f}")