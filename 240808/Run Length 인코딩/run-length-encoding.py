a = input()

# Run-Length Encoding을 위한 초기 변수 설정
key = a[0]
cnt = 1
arr = []

for i in range(1, len(a)):
    if key == a[i]:
        cnt += 1
    else:
        arr.append(f"{key}{cnt}")
        key = a[i]
        cnt = 1

# 마지막 문자와 그 개수를 배열에 추가
arr.append(f"{key}{cnt}")

# Run-Length Encoding 결과 문자열
encoded_str = ''.join(arr)

# 결과 출력
print(len(encoded_str))
print(encoded_str)