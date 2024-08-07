n = int(input())
arr =[]
for i in range(n):
    string = input()
    arr.append(string)
key = input()
cnt =0
sum =0
for j in arr:
    if j[0] ==key:
        cnt +=1
        sum += len(j)

print(f"{cnt} {(sum/cnt):.2f}")