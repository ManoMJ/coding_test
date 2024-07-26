def solution(elements):
    sums = set()
    c_elements = elements*2
    for i in range(1, len(elements)+1):
        for j in range(len(elements)):
            sub_sum = sum(c_elements[j: j+i])
            sums.add(sub_sum)
    return len(sums)


print(solution([7, 9, 1, 1, 4]))