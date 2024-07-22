a, b= map(int, input().split())
k =1
for i in range(a, b+1):
    k *=i
print(k)