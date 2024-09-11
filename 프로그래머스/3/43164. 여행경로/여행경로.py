def solution(tickets):
    memo = {}
    
    # 티켓을 정리하여 출발지마다 목적지를 리스트로 저장
    for src, dst in tickets:
        if src not in memo:
            memo[src] = [dst]
        else:
            memo[src].append(dst)
    
    # 목적지 리스트를 사전순으로 정렬
    for key in memo:
        memo[key].sort(reverse=True)
    
    path = []
    
    def dfs(node):
        while node in memo and memo[node]:
            dfs(memo[node].pop())
        path.append(node)
    
    dfs('ICN')
    return path[::-1]
