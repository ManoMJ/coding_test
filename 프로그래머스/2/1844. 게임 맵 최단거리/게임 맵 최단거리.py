from collections import deque

def solution(maps):
    dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    n = len(maps[0])
    m = len(maps)
    queue = deque([(0,0)])
    visited = [[0] * n for _ in range(m)]
    visited[0][0] = 1
    while queue:
        pos = queue.popleft()
        if pos == (m-1, n-1):
            return visited[pos[0]][pos[1]]
        moves = [(x+pos[0], y+pos[1]) for x,y in dirs]
        for x, y in moves:
            if 0<= x < m and 0 <= y < n and maps[x][y] == 1:
                if visited[x][y] == 0 :
                    visited[x][y] = visited[pos[0]][pos[1]] + 1
                    queue.append((x, y))

    return -1

maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
print(solution(maps))