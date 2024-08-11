n = int(input())
arr = list()
for i in range(n):
    given_str = input().split()
    if given_str[0] =="push_back":
        arr.append(given_str[1])
    elif given_str[0] =="pop_back":
        arr.pop()
    elif given_str[0] == "size":
        print(len(arr))
    elif given_str[0] =="get":
        key = int(given_str[1])
        print(arr[key-1])