given_str = input()
request = input()

for i in range(len(request)):
    if request[i] == "L":
        given_str = given_str[1:] + given_str[0]
    elif request[i] =="R":
        given_str = given_str[-1] + given_str[:-1]

print(given_str)