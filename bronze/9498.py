# 시험 성적

score = int(input())

if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
elif score >= 60:
    print('D')
else:
    print('F')


# 입력 1개는 split() 쓰면 x
# 문제에서 0~100 보장하기 때문에 따로 검사 안 해도 됨
# 조건은 위에서부터 순서대로
