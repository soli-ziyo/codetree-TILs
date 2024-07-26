score = list(map(float, input().split()))
sum =0

for i in score:
    sum +=i

k = len(score)
mean = sum /k 

print(f"{mean:.1f}")