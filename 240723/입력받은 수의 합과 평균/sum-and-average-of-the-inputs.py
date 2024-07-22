n = int(input())

sum = 0
for i in range(n):
    k = int(input())
    sum +=k

print(f"{sum} {(sum/n):.1f}")