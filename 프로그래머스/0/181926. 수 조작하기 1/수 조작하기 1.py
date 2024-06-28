def solution(n, control):
    con_list=list(control)
    for i in range(len(con_list)):
        if con_list[i]=='w':
            n+=1
        elif con_list[i]=='s':
            n-=1
        elif con_list[i]=='d':
            n+=10
        elif con_list[i]=='a':
            n-=10
    return n