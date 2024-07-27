arr = ['L','E','B','R','O','S']

n = input()

idx = -1

for i, char in enumerate(arr):
    if char ==n:
        idx =i

if idx ==-1:
    print("None")
else:
    print(idx)