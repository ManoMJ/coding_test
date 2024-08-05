from collections import deque

def solution(x, y, n):
    if x==y:
        return 0
    visited=set()
    q=deque([(x,0)])
    while q:
        top, seq =q.popleft()
        #visited.add(top)
        
        res =[top+n, 2*top, 3*top]
        for r in res:
            if r==y:
                return seq+1
            if r <= y and r not in visited:
                visited.add(r)
                q.append((r, seq+1))
    if not q:
        return -1