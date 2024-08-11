n = int(input())
sum = 0

for i in range(n):
    given_str = input()
    sum += int(given_str)
    
sum = str(sum)
sum = sum[1:] + sum[0]
print(sum)