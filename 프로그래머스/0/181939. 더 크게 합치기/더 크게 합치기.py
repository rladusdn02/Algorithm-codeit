def solution(a, b):
    a=str(a)
    b=str(b)
    an1=int(a+b)
    an2=int(b+a)
    if an1>=an2:
        return an1
    else:
        return an2