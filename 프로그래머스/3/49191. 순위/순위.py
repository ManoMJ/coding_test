def solution(n, results):
    axid = [ [0]*n for _ in range(n) ]
    
    for v1, v2 in results:
        axid[v1-1][v2-1] = 1
        axid[v2-1][v1-1] = -1
    
    winners = []
    losers = []
    for i, row in enumerate(axid):
        winners.clear()
        losers.clear()
        for j, cell in enumerate(row):
            if j != i and cell < 0:
                winners.append(j+1)
            elif j != i and cell > 0:
                losers.append(j+1)
        while losers:
            loser = losers.pop()
            for winner in winners:
                if axid[loser-1][winner-1] == 0:
                    axid[loser-1][winner-1] = -1
                    axid[winner-1][loser-1] = 1

    cnt = 0
    for row in axid:
        if row.count(0) == 1:
            cnt += 1
    return cnt


print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))