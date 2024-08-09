given_str = input()

str_list = list(given_str)

for i in range(len(str_list)):
    if i ==1 or i == len(str_list)-2 :
        str_list[i] = 'a'

given_str = ''.join(str_list)

print(given_str)