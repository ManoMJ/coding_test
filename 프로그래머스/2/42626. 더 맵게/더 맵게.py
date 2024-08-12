import heapq
min_heap = []
def solution(scoville, K):
    answer = 0
    if len(scoville) == 0:
        return -1
    
    for food in scoville:
        heapq.heappush(min_heap, food)
    
    while len(min_heap) >= 2 and min_heap[0] < K:
        first = heapq.heappop(min_heap) 
        second = heapq.heappop(min_heap)
        item = first + second*2
        heapq.heappush(min_heap, item)
        answer+=1
    
    if min_heap[0] < K:
        return -1
    
    return answer