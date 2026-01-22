# 두 수 비교하기

a, b = input().split()
a = int(a)
b = int(b)

if a > b:
    print('>')
elif a < b:
    print('<')
else:
    print('==')


# 조건문 기본 구조
# 비교 전에 반드시 int()