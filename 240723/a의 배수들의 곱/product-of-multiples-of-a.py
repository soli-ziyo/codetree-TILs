a, b = map(int, input().split())
k =1
for i in range(1, b+1):
    if i%a ==0:
        k *=i

print(k)