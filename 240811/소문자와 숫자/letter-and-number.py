given_str = input()
str_list = list(given_str)

for i in str_list:
    if i.isdigit():
        print(i, end='')
    elif i.isalpha():
        if i >= "A" and i <="Z":
            str1 = ord(i) - ord("A") +ord("a")
            print(chr(str1), end='')
        else:
            print(i, end='')