def solution(myString, pat):
    answer = 0
    mystr=myString.lower()
    p=pat.lower()
    if p in mystr:
        answer=1
    return answer