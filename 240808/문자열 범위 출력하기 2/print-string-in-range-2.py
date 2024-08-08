given_str = input()
n = int(input())

for i in given_str[:-n-1:-1]:
    print(i, end='')