cnt= [0] *5 

for i in range(1, 4):
    arr = list(input().split())

    if arr[0] =="Y" and int(arr[1]) >=37:
        cnt[1] +=1
    elif arr[0] =='N' and int(arr[1]) >=37:
        cnt[2] +=1
    elif arr[0] =="Y" and int(arr[1]) <37:
        cnt[3] +=1
    else:
        cnt[4] +=1
    
for j in range(1,5):
    print(cnt[j], end=' ')

if int(cnt[1]) >=2:
    print("E")