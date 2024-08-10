str1 = input()

str_list = list(str1)
key1 = str_list[0]
key2 = str_list[1]

for i in range(len(str_list)):
    if key1 == str_list[i]:
        str_list[i] = key2
    
    else:
        if key2 == str_list[i]:
            str_list[i] = key1
given_str = ''.join(str_list)
print(given_str)