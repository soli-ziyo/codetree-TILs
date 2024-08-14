def three(i):
    return i %3 ==0

def is_magic_num(i):
    ten = i//10 ; one = i%10
    return ten ==3 or ten ==6  or ten ==9 or three(i) or one==3 or one==6 or one==9


a, b = map(int, input().split())
cnt = 0
for i in range(a, b+1):
    if is_magic_num(i):
        cnt +=1
print(cnt)