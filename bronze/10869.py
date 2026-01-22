# 사칙연산
# 처음 틀린 이유 print(int(a) / int(b))  # ❌

a, b = input().split()
a = int(a)
b = int(b)

print(a + b)
print(a - b)
print(a * b)
print(a // b)  # 정수 나눗셈
print(a % b)

# / -> 실수 x
# // -> 정수 몫 o
# 출력 줄 수, 순서 중요