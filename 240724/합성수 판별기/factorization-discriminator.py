n = int(input())
yn =False

for i in range(2, n):
    if n %i ==0:
        yn = True
        break
    else:
        yn = False

if yn ==True:
    print("C")
else:
    print("N")