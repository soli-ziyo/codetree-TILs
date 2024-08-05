arr_2d = []

for i in range(2):
    arr_1d = list(map(int, input().split()))
    arr_2d.append(arr_1d)
    average = sum(arr_1d) /4
    print(f"{average:.1f}", end=' ')
print('')
k =0 

for i in range(1):
    for j in range(4):
                k = arr_2d[i][j] + arr_2d[i+1][j]
                average = k/ 2
                print(f"{average:.1f}", end=' ')
            
print('')

k=0
for i in range(2):
    for j in range(4):
        k +=arr_2d[i][j]
        
average = k/8 
print(f"{average:.1f}", end=' ')