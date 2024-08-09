def solution(storey):
    answer = 0
    mul = 10
    while storey != 0:
        m = storey % mul
        mid = mul//2
        if m > mid:
            storey += (10-m)
            answer += (10-m)
        elif 0 < m < mid:
            storey -= m
            answer += m
        elif m==mid:
            if (storey - m) // 10 % mul >= 5:
                storey += (10-m)
                answer += (10-m)
            else:
                storey -= m
                answer += m
        storey //= 10
        
    return answer