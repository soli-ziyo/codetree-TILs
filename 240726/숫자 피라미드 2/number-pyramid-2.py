n = int(input())
cnt =0

for i in range(n):
    for j in range(i+1):
        print(cnt+1, end=' ')
        cnt +=1
    print()