def solution(num_list):
    n=len(num_list)
    num_li_fin=[]
    last=num_list[n-1]
    front=num_list[n-2]
    if last>front:
        add=last-front
    elif last<=front:
        add=2*last
    num_list.append(add)
    return num_list