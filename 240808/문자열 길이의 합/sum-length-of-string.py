n = int(input())
arr = []
for i in range(n):
    string = input()
    arr.append(string)
str_len = 0
cnt=0
for j in arr:
    str_len +=len(j)
    if j[0] =="a":
        cnt +=1

print(str_len, cnt)