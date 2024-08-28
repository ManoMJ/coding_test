def solution(param):
    def timeToMinuts(time):
        time = list(map(int, time.split(':')) )
        return time[0]*60 + time[1]

    book_time = []
    for start, end in param:
        start = timeToMinuts(start)
        end = timeToMinuts(end) + 10
        book_time.append( [start, end] )
        
    print(book_time)
    book_time.sort(key=lambda x:x[0])
    rooms = []
    for start, end in book_time:
        if rooms:
            flag = False
            for room in rooms:
                if start >= room[-1][1]:
                    flag = True
                    room.append( (start, end) )
                    break
            if not flag:
                rooms.append( [(start, end)] )
        else:
            rooms.append( [(start, end)] )
    return len(rooms)

book_time = [["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]
print(solution(book_time))


