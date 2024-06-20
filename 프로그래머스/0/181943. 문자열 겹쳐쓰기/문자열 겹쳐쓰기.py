def solution(my_string, overwrite_string, s):
    list1=list(my_string)
    list2=list(overwrite_string)
    for i in range(0, len(list2)):
        list1[s]=list2[i]
        s=s+1
    answer=''.join(list1)
    return answer