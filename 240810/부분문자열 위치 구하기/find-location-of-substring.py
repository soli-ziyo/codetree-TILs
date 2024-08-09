given_str = input()
key = input()
cnt1 =0

if key in given_str:
    k = given_str.find(key)
    str_list = list(given_str)
    str_list.pop(k)
    new_str = ''.join(str_list)
    k = 1
else:
    k = -1

if k != -1:
    if key == given_str:
        k = 0
    if key in new_str:
        k = new_str.find(key) -1

print(k)