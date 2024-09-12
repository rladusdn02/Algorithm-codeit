# def solution(participant, completion):
#     answer = ''
#     for p in participant:
#         if p in completion:
#             continue
#         else:
#             answer+=p
#     return answer
# → 테스트케이스 1,2만 통과(동명이인 처리 불가)

def solution(participant, completion):
    answer = ''
    rundict={} #참가자를 dictionary로 바꾸면서 사용할 dictionary
    for p in participant: #루프를 돌며 참가자 확인
        if p in rundict: #동명이인이 있다면
            rundict[p]+=1 #해당 value를 1더함
        else: #동명이인이 없다면
            rundict[p]=1 #기본값인 1로 설정
            
    for c in completion: #루프를 돌며 참자가 확인
        if c in rundict: #참가자가 완주했다면
            rundict[c]-=1 #해당 value를 1뺌
    for p in rundict: #참가자 딕셔너리에 남은사람이 있는지 검사
        if rundict[p]>0: #value가 1이상인 참가자가 있다면
            return p #리턴
    return answer