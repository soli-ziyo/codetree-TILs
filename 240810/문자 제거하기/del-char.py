given_str = input()
str_list = list(given_str)
rangenum = len(str_list)
num = 0
for i in range(rangenum):
    num = int(input())
    if num <= len(str_list):
        str_list.pop(num)
        str1= ''.join(str_list)
        print(str1)
    else:
        str_list.pop(-1)
        str1= ''.join(str_list)
        print(str1)
        break