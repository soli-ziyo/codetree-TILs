n = int(input())
sum =0
cnt =0
for i in range(n):
    score = list(map(int, input().split()))

    for j in score:
        sum += j 
        mean = sum/4
    if mean >=60:
        print("pass")
        #print(mean)
        cnt +=1
    else:
        print("fail")
    sum=0
print(cnt)