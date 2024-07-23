sum =0
cnt =0
while True:
    n = int(input())
    if n //10 ==2:
        cnt +=1
        sum +=n
        mean = sum /cnt
    else:
        break
print(f"{mean:.2f}")