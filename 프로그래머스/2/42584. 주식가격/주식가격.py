def solution(prices):
    answer = [0] * len(prices)
    for i, p in enumerate(prices):
        cnt = 0
        for j in range(i+1, len(prices)):
            cnt+=1
            if prices[j] < p:
                break
        answer[i] = cnt
    return answer

print(solution([1, 2, 3, 2, 3]))