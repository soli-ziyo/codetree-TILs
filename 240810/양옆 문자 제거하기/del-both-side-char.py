given_str = input()

str_list = list(given_str)
str_list.pop(2); str_list.pop(-2)

given_str= ''.join(str_list)

print(given_str)