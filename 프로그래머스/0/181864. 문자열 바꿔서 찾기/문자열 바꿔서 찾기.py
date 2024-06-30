def solution(myString, pat):
    answer = 0
    new=[]
    for i in range(len(myString)):
        if myString[i]=="A":
            new.append("B")
        elif myString[i]=="B":
            new.append("A")
    myString="".join(new)
    if pat in myString:
        answer=1
    return answer