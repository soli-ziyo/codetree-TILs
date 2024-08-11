given_str = input()
str_list = list(given_str)
cnt =0

for i in str_list:
    if i.isdigit():
        cnt += int(i)
print(cnt)