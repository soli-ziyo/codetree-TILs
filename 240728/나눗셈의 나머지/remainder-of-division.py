arr = list(map(int, input().split() ))
cnt =[0] *11
sum =0

while True:
    if arr[0] >1:
        a = arr[0] // arr[1] 
        b =arr[0] % arr[1] 
        cnt[b] +=1
        arr[0] = a    
    else:
        break

for i in cnt:
    sum += i**2

print(sum)