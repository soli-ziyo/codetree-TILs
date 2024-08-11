a, b = input().split()
given_str = str(int(a)+int(b))

str_list = list(given_str)
cnt = 0
for i in str_list:
    if i =="1" :
        cnt +=1

print(cnt)