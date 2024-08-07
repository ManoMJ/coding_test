import heapq

def solution(operations):
    answer = []
    min_heap = []
    max_heap = []
    valids = set()
    count=0
    for op in operations:
        act, num = op.split()
        num = int(num)
        if act == 'I':
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -num)
            valids.add(num)
            count+=1
        elif act == "D":
            if num == 1 and not count==0:    # 최대 삭제
                count-=1
                while max_heap:
                    item = -heapq.heappop(max_heap)
                    if item in valids:
                        valids.remove(item)
                        break
            elif num == -1 and not count==0: # 최소 삭제
                count-=1
                while min_heap:
                    item = heapq.heappop(min_heap)
                    if item in valids:
                        valids.remove(item)
                        break
    
    if count == 0:
        return [0, 0]
    
    mx = mn = 0
    while max_heap:
        mx = -max_heap[0]
        if mx in valids:
            break
        heapq.heappop(max_heap)
    
    while min_heap:
        mn = min_heap[0]
        if mn in valids:
            break
        heapq.heappop(min_heap)
        
    return [mx, mn]