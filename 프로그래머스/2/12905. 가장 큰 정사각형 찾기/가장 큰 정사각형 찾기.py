def solution(board):
    m = len(board[0])
    n = len(board)
    dp = [ [0] * m for _ in range(n)]
    max_side = 0
    
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell == 1:
                if i==0 and j==0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    if dp[i][j] > max_side:
                        max_side = dp[i][j]
        
    if max_side==0:
        for row in board:
            if sum(row) >= 1:
                max_side=1
                break
                
    return max_side ** 2
