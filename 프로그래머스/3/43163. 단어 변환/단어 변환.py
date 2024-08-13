from collections import deque

def get_diff(begin, target):
    cnt = 0
    for i in range(len(begin)):
        if begin[i] != target[i]:
            cnt+=1
        if cnt >= 2:
            return False
    if cnt==0:
        return False
    return True

def solution(begin, target, words):
    answer = 0
    if target not in words:
        return answer
    visited = set()
    queue = deque([])
    for word in words:
        if get_diff(begin, word):
            queue.append((word, 1))
            visited.add(word)
            break
    
    while queue:
        node, dist = queue.popleft()
        if node  == target:
            return dist
        for word in words:
            if word not in visited and get_diff(node, word):
                queue.append( (word, dist + 1) )
                visited.add(word)
    return answer

begin="hit"	
target = "cog"	
words = ["hot", "dot", "dog", "lot", "log", "cog"]
print(solution(begin, target, words))