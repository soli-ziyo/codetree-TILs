n = int(input())
cnt =0
for i in range(n):
    for j in range(i):
        print(' ', end=' ')
    for j in range(n-i):
        if cnt ==9:
            cnt =0
            print(cnt+1, end=' ')
        else:
            print(cnt+1, end=' ')
        cnt +=1
    print()