n = int(input())
sum = 0
for i in range(n):
    k = int(input())
    if k %2 !=0 and k %3 ==0:
        sum +=k
print(sum)