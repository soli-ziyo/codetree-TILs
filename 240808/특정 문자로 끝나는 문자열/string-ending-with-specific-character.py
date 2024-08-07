arr =[]
for i in range(10):
    string = input()
    arr.append(string)
n = input()
cnt = 0
for j in arr:
    if j[-1] == n :
        print(j)
        cnt +=1

if cnt ==0:
        print("None")