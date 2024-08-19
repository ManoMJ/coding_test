from collections import deque 

def solution(bridge_length, weight, truck_weights):
    tm = 0
    n = len(truck_weights)
    status = [bridge_length] * n
    start=0
    end = 0
    cur = deque()
    
    while status[n-1] > 0:

        for i in range(start, end):
            if status[i] > 0:
                status[i] -= 1
            if status[i] == 0 and cur:
                cur.popleft()
                start+=1
        if end < n and sum(cur) + truck_weights[end] <= weight:
            cur.append(truck_weights[end])
            end+=1
        tm+=1
    return tm

bridge_length = 100
weight = 100
truck_weights = [10,10,10,10,10,10,10,10,10,10]
print(solution(bridge_length, weight, truck_weights))