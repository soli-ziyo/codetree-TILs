a, b = map(int, input().split())

def print_gugudan(a, b):
    # 순서: b단부터 a단까지 출력
    for i in range(2, 10, 2):
        line_parts = []
        for j in range(b, a-1, -1):
            result = j * i
            line_parts.append(f"{j} * {i} = {result}")
        print(" / ".join(line_parts))

# 구구단 출력
print_gugudan(a, b)