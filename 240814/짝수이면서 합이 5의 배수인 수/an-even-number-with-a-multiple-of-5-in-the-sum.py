def is_magic_number(n):
    ten= n //10 ; one = n % 10
    return n %2 ==0 and (ten+one) %5 ==0

n = int(input())

if is_magic_number(n):
    print("Yes")
else:
    print("No")