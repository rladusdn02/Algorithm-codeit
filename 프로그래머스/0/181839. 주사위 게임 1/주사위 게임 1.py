def solution(a, b):
    answer = 0
    if a % 2 == 1 or b % 2 == 1:  # 둘 중 하나가 홀수인 경우
        if a % 2 == 1 and b % 2 == 1:  # 둘 다 홀수인 경우
            answer = a ** 2 + b ** 2
        else:  # 둘 중 하나만 홀수인 경우
            answer = 2 * (a + b)
    else:  # 둘 다 짝수인 경우
        answer = abs(a - b)
    return answer