cold1, temp1 = input().split()
cold2, temp2= input().split()
cold3, temp3 = input().split()

temp1, temp2, temp3 = int(temp1), int(temp2), int(temp3)

if (cold1 == "Y" and temp1 >=37):
    if (cold2 == "Y" and temp2>=37):
        print("E")
    elif (cold3 == "Y" and temp3>=37):
        print("E")
    else:
        print("N")
elif (cold2 =="Y" and temp2 >=37):
    if (cold1 == "Y" and temp1>=37):
        print("E")
    elif (cold3 == "Y" and temp3>=37):
        print("E")
    else:
        print("N")
elif (cold3 =="Y" and temp3 >=37):
    if (cold1 == "Y" and temp1>=37):
        print("E")
    elif (cold2 == "Y" and temp2>=37):
        print("E")
    else:
        print("N")