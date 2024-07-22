def solution(s):
    answer = True
    pcnt = 0
    ycnt = 0
    for char in s:
        if char in 'yY':
            ycnt += 1
        elif char in 'pP':
            pcnt += 1
    if pcnt == ycnt:
        return True
    else:
        return False

s = "pPoooyY"
