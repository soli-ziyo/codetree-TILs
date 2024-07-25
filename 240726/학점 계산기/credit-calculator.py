n = int(input())

score = list(map(float, input().split()))
sum =0

for i in range(n):
    sum += score[i]

mean = sum / n

print(f"{mean:.1f}")
if mean >=4.0:
    print("Perfect")
elif mean >=3.0:
    print("Good")
else:
    print("Poor")