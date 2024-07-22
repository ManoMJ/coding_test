def solution(cards):
    answer = 0
    n = len(cards)
    visited = [False] * n
    groups = []
    
    for i in range(n):
        if not visited[i]:
            group = []
            group.append(cards[i])
            cur = cards[i] - 1
            visited[i] = True
            while not visited[cur]:
                visited[cur] = True
                cur = cards[cur] - 1
                group.append(cards[cur])
            groups.append(len(group))
    
    if len(groups) < 2:
        return 0
    
    groups.sort(reverse=True)
    
    answer = groups[0] * groups[1]
    return answer

cards = [8, 6, 3, 7, 2, 5, 1, 4]