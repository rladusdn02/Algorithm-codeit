def solution(numLog):
    num_list = list(numLog)
    result_list=[]
    for i in range(1, len(num_list)):
        if num_list[i]-1==num_list[i-1]:
            result_list.append('w')
        elif num_list[i]+1==num_list[i-1]:
            result_list.append('s')
        elif num_list[i]-10==num_list[i-1]:
            result_list.append('d')
        elif num_list[i]+10==num_list[i-1]:
            result_list.append('a')
    return ''.join(result_list)