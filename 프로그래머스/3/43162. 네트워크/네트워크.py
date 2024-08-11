from collections import deque

def solution(n, computers):
    visited = set()
    q = deque([])
    answer = 0
    for i in range(n):
        if i not in visited:
            visited.add(i)
            answer +=1
            q.append(i)
            while q:
                top = q.popleft()
                visited.add(top)
                cur=computers[top]
                for j in range(len(cur)):
                    if cur[j] == 1 and j not in visited:
                        q.append(j)
                        
                
        
    return answer