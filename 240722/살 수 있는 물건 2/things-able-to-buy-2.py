n = int(input())

book = 3000
mask = 1000
pen = 500

if n >=3000:
    print("book")
elif 1000<=n<3000:
    print("mask")
elif 500<=n<1000:
    print("pen")
else:
    print("no")