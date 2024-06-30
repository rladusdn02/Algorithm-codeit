def solution(todo_list, finished):
    answer=[]
    for i in range(len(finished)):
        if finished[i]==1:
            continue
        else:
            answer.append(todo_list[i])
    return answer