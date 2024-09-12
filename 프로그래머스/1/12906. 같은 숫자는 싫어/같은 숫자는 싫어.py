def solution(arr):
    answer = []
    for i in range(len(arr)):
        if i == 0 or arr[i] != arr[i-1]:  # 첫 번째 요소는 무조건 추가, 그 이후는 이전 값과 비교
            answer.append(arr[i])
    return answer