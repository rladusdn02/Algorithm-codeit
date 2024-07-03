def solution(n):
    #일단 모든 원소를 n*n 배열로 생성
    arr = [[0] * n for _ in range(n)]
    for i in range(n):
        #대각선요소면 1
        arr[i][i] = 1
    return arr