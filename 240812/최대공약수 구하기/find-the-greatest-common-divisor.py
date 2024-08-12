def key(n, m):
    if n >=m:
        for i in range(m, 0, -1):
            if n%i ==0 and m%i ==0:
                print(i)
                break
            else:
                continue
    else:
        for i in range(n, 0, -1):
            if n%i ==0 and m%i ==0:
                print(i)
                break
            else:
                continue 

n, m = map(int, input().split())
key(n,m)