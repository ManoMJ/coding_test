def solution(n, times):
    low = 0
    high = max(times) * n
    mn = min(times)
    answer = high
    
    while low <= high:
        total = 0
        mid = (low + high) // 2
        
        for time in times:
            total += mid // time
            
        if total < n:
            low = mid+1
        if total >= n:
            answer = mid
            high = mid-1
            
    return answer