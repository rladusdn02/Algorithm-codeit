def solution(n):
    result=0
    k=int(n/2) #n을 2로 나누었을 때 몫
    for i in range(0,k+1):
        if n % 2 == 1: #홀수일때
            a=2*i+1
        else:
            a=(2*i)**2
        result+=a
    return result