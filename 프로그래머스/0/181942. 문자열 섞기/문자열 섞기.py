def solution(str1, str2):
    list1=list(str1)
    list2=list(str2)
    ans_list=[]
    for i in range(len(list1)):
        ans=list1[i]+list2[i]
        ans_list+=str(ans)
    ans_list=''.join(ans_list)
    return ans_list