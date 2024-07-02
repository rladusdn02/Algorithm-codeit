def solution(myString):
    answer = ''
    for i in myString:
        i = i.lower()
        if i == 'a':
            answer+=i.upper()
        else:
            answer+=i.lower()
    return answer