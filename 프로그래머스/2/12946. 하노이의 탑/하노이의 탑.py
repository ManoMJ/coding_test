def solution(n):
    def hanoii(start, mid, end, n, moves):
        if n==1:
            moves.append([start, end])
            return
        hanoii(start, end, mid, n-1, moves)
        moves.append([start, end])
        hanoii(mid, start, end, n-1, moves)
    
    moves = []
    hanoii(1, 2, 3, n, moves)
    return moves
