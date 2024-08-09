given_str = input()
key = input()
cnt =0
for i in range(len(given_str)-1):
    if given_str[i] == key[0] and given_str[i+1] == key[1]:
        cnt +=1

print(cnt)