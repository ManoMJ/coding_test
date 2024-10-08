from collections import deque
from collections import defaultdict

def solution(n, edge):
    answer = 0
    memo = defaultdict(list)
    for s, e in edge:
        memo[s].append(e)
        memo[e].append(s)
    
    q = deque([(1,0)])
    visited = set()
    visited.add(1)
    memo2 = defaultdict(list)
    
    while q:
        top, dist = q.popleft()
        for neighbor in memo[top]:
            if neighbor not in visited:
                visited.add(neighbor)
                q.append( (neighbor, dist+1 ))
                memo2[dist+1].append(neighbor)
    mx=max(memo2) 
    if mx==0:
        return 0
    return len(memo2[mx])