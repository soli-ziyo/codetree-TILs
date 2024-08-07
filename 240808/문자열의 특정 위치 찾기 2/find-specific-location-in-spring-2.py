str1 = ["apple", "banana","grape", "blueberry", "orange"]
key = input()
cnt = 0
for i in range(5):
    if str1[i][2] == key or str1[i][3] == key:
        print(str1[i])
        cnt +=1 
print(cnt)