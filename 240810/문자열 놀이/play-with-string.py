given_str, q = input().split() ; q = int(q)
str_list=[]

for i in range(q):
    num, a, b = input().split()
    num = int(num)
    str_list = list(given_str)

    if num == 1:
        a= int(a) ; b = int(b)
        temp = str_list[a-1]
        str_list[a-1] = str_list[b-1]
        str_list[b-1] = temp
        given_str = ''.join(str_list) 
        print(given_str)
    if num == 2:
        for j in range(len(str_list)):
            if str_list[j] == a:
                str_list[j] = b
                given_str=''.join(str_list)
        print(given_str)