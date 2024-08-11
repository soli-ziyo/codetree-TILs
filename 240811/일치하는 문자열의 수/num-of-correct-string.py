n, A = input().split()
n = int(n)
cnt = 0
for i in range(n):
    given_str = input()
    if given_str == A :
        cnt +=1

print(cnt)