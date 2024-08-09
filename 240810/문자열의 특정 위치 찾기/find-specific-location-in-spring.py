given_str, key = input().split()

if key in given_str:
    print(given_str.index(key))
else:
    print("No")