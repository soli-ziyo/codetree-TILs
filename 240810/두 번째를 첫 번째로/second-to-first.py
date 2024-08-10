given_str= input()
key1 = given_str[0]
key2 = given_str[1]

str_list=list(given_str)

for i in range(len(str_list)):
    if str_list[i] == key2:
        str_list[i] = key1
given_str = ''.join(str_list)

print(given_str)