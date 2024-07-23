n = int(input())

for i in range(n):
    for j in range(n-i):
        k = n-i
        while k >=1:
            print("*", end='')
            k -=1
        while k ==0:
            print("", end=' ')
            break
    print()