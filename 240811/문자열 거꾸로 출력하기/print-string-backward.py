while True:
    str1 =input()
    if str1 == "END":
        break
    else:
        for i in str1[::-1]:
            print(i, end='')
        print()