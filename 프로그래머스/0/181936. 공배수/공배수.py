def solution(numb, n, m):
    cal1=numb%n
    cal2=numb%m
    if cal1==0 and cal2==0:
        return 1
    else:
        return 0