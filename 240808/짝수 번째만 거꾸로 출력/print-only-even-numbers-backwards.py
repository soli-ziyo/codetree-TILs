given_str = input()
arr=""

for i in range(len(given_str)):
    if (i+1) %2 ==0:
        arr +=given_str[i]
    else:
        continue

for j in arr[::-1]:
    print(j, end='')