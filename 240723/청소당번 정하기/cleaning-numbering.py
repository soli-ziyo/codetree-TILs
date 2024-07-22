n = int(input())
cnt1= 0
cnt2= 0
cnt3= 0
for i in range(1, n+1): #i의 숫자 몇부터 시작할지 지정할 수 있음 
    if i %12 ==0:#가장 위에서부터 쓰는것이 우선순위 높은 것! 
        cnt3 +=1
    elif i %3 ==0:
        cnt2 +=1
    elif i%2 ==0:
        cnt1 +=1
print(cnt1, cnt2, cnt3)