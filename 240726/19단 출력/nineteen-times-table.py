for i in range(1, 20):
    for j in range(1,20):
        

        if j%2!=0 :
            print(f"{i} * {j} = {i*j}", end=' ')
            if j==19:
                print('', end='')
            else:
                print("/", end=' ')
        else:
            print(f"{i} * {j} = {i*j}", end='\n')
    print()