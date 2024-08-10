a = input()
b = input()
lenb = len(b)

while True:
    str_list = list(a)
    if b in a:
        k = a.find(b)
        str_list = str_list[:k] + str_list[k+lenb:]
        a = ''.join(str_list)

    else:
        a = ''.join(str_list)
        print(a)
        break