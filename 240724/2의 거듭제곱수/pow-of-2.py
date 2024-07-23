n = int(input())
cnt =0

while True:
    if n //2 !=1:
        cnt +=1
        n= n//2
    else:
        cnt +=1
        break

print(cnt)