def solution(players, callings):
    answer = []
    srch = {}
    for index, player in enumerate(players):
        srch[player] = index
    for char in callings:
        if char in srch:
            idx = srch[char]
        else:
            idx = players.index(char)
            
        if idx > 0:
            players[idx-1], players[idx] = players[idx], players[idx-1]
            srch[players[idx-1]] = idx-1
            srch[players[idx]] = idx
            
    return players