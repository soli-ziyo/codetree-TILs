n = int(input())
yn = True #소수인 경우 
for i in range(2,n):
    if n %i ==0:
        yn = False #소수가 아닌 경우
        break
    else:
        yn = True #소수인 경우 

if yn ==True:
    print("P")
else:
    print("C")