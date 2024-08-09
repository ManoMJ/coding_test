def solution(storey):
    answer = 0
    mul = 10
    while storey != 0:
        print(storey)
        m = storey % mul
        mid = mul//2
        digit = mul // 10
        if m > mid:
            storey += digit
            answer += 1
        elif 0 < m < mid:
            storey -= digit
            answer += 1
        elif m==mid:
            if storey // mul % 10 >= 5:
                storey += digit
                answer += 1
            else:
                storey -= digit
                answer += 1
        else:
            mul *= 10
        
    return answer

print(solution(5555))