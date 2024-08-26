def solution(places):
    def chk_right_pos(place, red_zones):
        for i, row in enumerate(place):
            for j, cell in enumerate(row):
                if cell == 'P':
                    for dx, dy in red_zones:
                        new_x = i+dx
                        new_y = j+dy
                        if 0 <= new_x < 5 and 0<= new_y < 5:
                            if place[new_x][new_y] == 'P':
                                return 0
                            if place[new_x][new_y] == 'O':
                                for ddx, ddy in red_zones:
                                    if 0 <= new_x + ddx < 5 and 0 <= new_y + ddy < 5:
                                        if (new_x+ddx, new_y+ddy) != (i, j) and place[new_x+ddx][new_y+ddy]=='P':
                                            return 0
        return 1
                        

    answer = [1] * len(places)
    red_zones = [[0,1], [1,0], [0,-1], [-1,0]]

    for p, place in enumerate(places):
        answer[p] = chk_right_pos(place, red_zones)
                            

    return answer

places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
print(solution(places))