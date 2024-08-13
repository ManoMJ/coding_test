def find_root(parent, v):
    if parent[v] != v:
        parent[v] = find_root(parent, parent[v])
    return parent[v]

def solution(n, costs):
    costs.sort(key = lambda x : x[2])
    
    parent = [i for i in range(n+1)]
    rank = [0] * (n+1)
    total_cost = total = 0
    for cost in costs:
        v1, v2, c = cost
        root1 = find_root(parent, v1)
        root2 = find_root(parent, v2)
        if root1 != root2:
            if rank[root1] > rank[root2]:
                parent[root2] = root1
            elif rank[root2] > rank[root1]:
                parent[root1] = root2
            else:
                parent[root2] = root1
                rank[root1] += 1
            total_cost += c
            total += 1
        
        if total == n-1:
            return total_cost
        
    return total_cost