import heapq
def solution(n, k, enemy):
    answer = 0
    heap = []
    for i in range(len(enemy)):
        heapq.heappush(heap, -enemy[i])
        n -= enemy[i]
        if n < 0:
            if k > 0:
                k-=1
                n += (-heapq.heappop(heap))
            else:
                return i
            
    return len(enemy)
        