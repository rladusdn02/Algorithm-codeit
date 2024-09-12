import math

def solution(progresses, speeds):
    answer = []
    days = []
    
    # 각 작업의 완료까지 남은 일수 계산
    for i in range(len(progresses)):
        p = 100 - progresses[i]
        s = speeds[i]
        days.append(math.ceil(p / s))
    
    print(days)  # 디버깅용 출력
    
    cnt = 1  # 첫 번째 작업은 무조건 포함되므로 1부터 시작
    current_day = days[0]  # 첫 번째 작업의 배포 기준
    
    for j in range(1, len(days)):
        if days[j] <= current_day:  # 현재 작업이 앞의 작업과 같은 날에 배포 가능
            cnt += 1
        else:  # 새로운 배포 그룹 시작
            answer.append(cnt)  # 현재 그룹 크기 추가
            cnt = 1  # 새로운 그룹 시작
            current_day = days[j]  # 새로운 배포 기준일 업데이트
    
    # 마지막 그룹 추가
    answer.append(cnt)
    
    return answer