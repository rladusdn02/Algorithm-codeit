def solution(a, d, included):
    sum=0
    n = len(included)
    for i in range(n):
        if included[i] == True:
            sum=sum+(a+i*d)
        else:
            continue

    return sum