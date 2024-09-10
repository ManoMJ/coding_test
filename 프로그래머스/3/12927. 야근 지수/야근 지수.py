import heapq
def solution(n, works):
    if sum(works) <= n:
        return 0
    
    works = [-x for x in works]
    heapq.heapify(works)
    
    while n > 0:
        cur = heapq.heappop(works)
        heapq.heappush(works, cur+1)
        n -= 1
    
    return sum(x**2 for x in works)