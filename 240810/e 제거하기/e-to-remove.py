given_str = input()

k = given_str.find('e')
str_list = list(given_str)
str_list.pop(k)
given_str = ''.join(str_list)
print(given_str)