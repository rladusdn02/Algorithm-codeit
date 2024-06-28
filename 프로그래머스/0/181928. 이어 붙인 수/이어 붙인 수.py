def solution(num_list):
    odd_li=[]
    even_li=[]
    for i in range(len(num_list)):
        if num_list[i]%2==1:
            odd_li.append(str(num_list[i]))
        elif num_list[i]%2==0:
            even_li.append(str(num_list[i]))

    odd=''.join(odd_li)
    even=''.join(even_li)
    odd_fin=int(odd)
    even_fin=int(even)
    sum=odd_fin+even_fin
    return sum