from collections import deque

def solution(board):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    rows, cols = len(board), len(board[0])
    visited = [[False] * cols for _ in range(rows)]
    
    # 시작 위치(R)와 목표 위치(G) 찾기
    start, goal = None, None
    for i in range(rows):
        for j in range(cols):
            if board[i][j] == 'R':
                start = (i, j)
            elif board[i][j] == 'G':
                goal = (i, j)

    # BFS 큐 초기화
    queue = deque([(start[0], start[1], 0)])  # (x, y, 이동 횟수)
    visited[start[0]][start[1]] = True

    while queue:
        x, y, moves = queue.popleft()

        # 목표 지점에 도착하면 이동 횟수 반환
        if (x, y) == goal:
            return moves

        # 상, 하, 좌, 우로 이동
        for dx, dy in directions:
            nx, ny = x, y
            while 0 <= nx + dx < rows and 0 <= ny + dy < cols and board[nx + dx][ny + dy] != 'D':
                nx += dx
                ny += dy

            # 새로운 위치가 방문되지 않았다면 큐에 추가
            if not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, moves + 1))

    return -1  # 목표에 도달할 수 없는 경우