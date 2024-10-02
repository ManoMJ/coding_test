def solution(data, col, row_begin, row_end):
    data.sort(key=lambda x: (x[col-1], -x[0]))

    serial = []
    for i in range(row_begin-1, row_end):
        tmp = 0
        for j in data[i]:
            tmp += j % (i+1)
        serial.append(tmp)
    s = serial[0]
    for i in range(1, len(serial)):
        s = s ^ serial[i]
    return s
