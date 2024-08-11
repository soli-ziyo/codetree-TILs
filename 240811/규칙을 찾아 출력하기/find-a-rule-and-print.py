def print_pattern(n):
    if n == 1:
        print('*')
    elif n == 2:
        print('* *')
        print('* *')
    else:
        # 첫 번째 줄: n개의 별을 출력
        print('* ' * n)

        # 중간 줄: 패턴을 맞춰 별과 공백 출력
        for i in range(1, n-1):
            print('* ' * (i+1) + '  ' * (n-i-2) + '*')

        # 마지막 줄: n개의 별을 출력
        print('* ' * n)

# 예시 실행
n = int(input())
print_pattern(n)