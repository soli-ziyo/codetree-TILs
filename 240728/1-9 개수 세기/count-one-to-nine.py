n = int(input())

cnt =[0] * 10

mylist = list(map(int, input().split()))

for i in mylist:
    cnt[i] +=1

for j in range(1, 10):
    print(cnt[j])