yn = True
for i in range(5):
    n = int(input())

    if n % 3 ==0:
        yn = True
    else:
        yn = False
        break

if yn ==True:
    print(1)
else:
    print(0)