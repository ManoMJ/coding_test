def solution(triangle):
    n = len(triangle)
    memo={}
    for i in range(n-1, -1, -1):
        for j in range(0, len(triangle[i])):
            
            if i==n-1:
                memo[(i, j)] = triangle[i][j]
            else:
                memo[(i, j)] = max(triangle[i][j] + memo[(i+1, j)], triangle[i][j] + memo[(i+1, j+1)])
    
    return memo[(0,0)]

triangle=[[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(solution(triangle))