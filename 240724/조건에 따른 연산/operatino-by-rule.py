n = int(input())
cnt =0

while True:
    if n%2==0:
        n = 3*n +1
        cnt +=1
    else:
        n = 2*n +1
        cnt +=1
    
    if n >=1000:
        break

print(cnt)