def solution(topping):
    answer = 0
    len_of_tops = len(set(topping))
    first=[topping[0]]
    second=topping.copy()
    del second[0]
    second.reverse()
    first_set={topping[0]:1}
    second_set={}
    for n in second:
        if n in second_set:
            second_set[n]+=1
        else:
            second_set[n]=1
            
    for i in range(1, len(topping)):
        poped = second.pop()
        if poped in first_set:
            first_set[poped]+=1
        else:
            first_set[poped]=1
        if second_set[poped]==1:
            del second_set[poped]
        else:
            second_set[poped] -=1
        if len(first_set) == len(second_set):
            answer += 1
            
    return answer

