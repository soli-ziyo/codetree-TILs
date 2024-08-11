given_str = input()
str_list = list(given_str)

for i in str_list:
    if i >= "A" and i <= "Z":
        print(i.lower(), end='')
    else:
        print(i.upper(), end='')