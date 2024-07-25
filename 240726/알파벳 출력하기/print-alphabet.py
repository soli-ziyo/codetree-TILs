n = int(input())
cnt = ord("A")

for i in range(n):
    for j in range(i+1):
        if chr(cnt) =='Z':
            print(chr(cnt), end='')
            cnt =ord("A")

        else:
            print(chr(cnt), end='')
            cnt+=1
    print()