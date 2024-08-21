import heapq

def solution(jobs):
    jobs.sort(key = lambda x : x[0])
    heap = []
    tm = idx = answer = 0
    n = len(jobs)
    while idx < n or heap:
        while idx < n and jobs[idx][0] <= tm :
            heapq.heappush(heap, (jobs[idx][1], jobs[idx][0]))
            idx += 1
        if heap:
            cost, start = heapq.heappop(heap)
            tm += cost
            answer += (tm - start)
        else:
            tm = jobs[idx][0]
    return answer // n

# start, cost
jobs = [[0, 3], [1, 9], [2, 6]]
print(solution(jobs))