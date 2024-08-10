given_str = input()
str_list = list(given_str)
num = 0

while len(str_list) > 1:
    num = int(input())

    if num < len(str_list):
        str_list.pop(num)
    else:
        str_list.pop(-1)
        
    str1= ''.join(str_list)
    print(str1)