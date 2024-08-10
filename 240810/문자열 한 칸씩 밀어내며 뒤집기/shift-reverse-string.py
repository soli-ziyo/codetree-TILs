given_str , q = input().split() ; q = int(q)

for i in range(q):
    request = int(input())
    if request ==1:
        given_str = given_str[1:] + given_str[0]
        print(given_str)
    elif request ==2:
        given_str = given_str[-1] +given_str[:-1]
        print(given_str)
    elif request ==3:
        given_str = given_str[::-1]
        print(given_str)