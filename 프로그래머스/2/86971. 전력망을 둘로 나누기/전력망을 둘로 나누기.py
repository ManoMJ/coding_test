from collections import defaultdict



def solution(n, wires):
    
    def make_graph(wires):
        graph = defaultdict(list)
        for v1, v2 in wires:
            graph[v1].append(v2)
            graph[v2].append(v1)
        return graph
    
    def dfs(graph, start_node):
        cnt=0
        visited = set()
        stack = [start_node]
        while stack:
            top = stack.pop()
            visited.add(top)
            cnt+=1
            for neighbor in graph[top]:
                if neighbor not in visited:
                    stack.append(neighbor)

        return cnt

    min_diff = n
    graph = make_graph(wires)

    for v1, v2 in wires:
        graph[v1].remove(v2)
        graph[v2].remove(v1)

        cnt1 = dfs(graph, v1)
        cnt2 = dfs(graph, v2)

        if min_diff > abs(cnt1 - cnt2):
            min_diff = abs(cnt1 - cnt2)

        graph[v1].append(v2)
        graph[v2].append(v1)
    
    return min_diff

