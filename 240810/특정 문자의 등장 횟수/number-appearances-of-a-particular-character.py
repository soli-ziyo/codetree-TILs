given_str = input()
cnt1 = 0 ; cnt2 = 0
for i in range(len(given_str)-1):
    if given_str[i] =='e' and given_str[i+1] =='e':
        cnt1 +=1
    if given_str[i] =='e' and given_str[i+1] =='b':
        cnt2 +=1

print(cnt1, cnt2)