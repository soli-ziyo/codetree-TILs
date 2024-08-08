given_str = input()
key1 = "No" ; key2 = "No"
for i in range(len(given_str)-1):
    if given_str[i] == "e" and given_str[i+1] == "e":
        key1 = "Yes"
        break

for i in range(len(given_str)-1):
    if given_str[i] =="a" and given_str[i+1] =="b":
        key2 = "Yes"
        break

print(key1, key2)