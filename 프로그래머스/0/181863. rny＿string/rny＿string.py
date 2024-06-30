def solution(rny_string):
    answer = []
    for i in range(len(rny_string)):
        if "m" == rny_string[i]:
            answer.append("rn")
        else:
            answer.append(rny_string[i])
    answer="".join(answer)
    return answer