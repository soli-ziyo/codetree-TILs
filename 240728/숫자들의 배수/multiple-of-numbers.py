n = int(input())

mylist =[]
cnt =0

for i in range(1, 11):
    k = n *i
    print(k, end=' ')

    if k % 5==0:
        cnt +=1

    if cnt ==2:
        break