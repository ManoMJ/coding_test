def solution(s):
    turn = cnt = 0
    while s != '1':
        turn += 1
        n = len(s)
        idx = 0
        copied = ''
        while idx < n:
            if s[idx] == '0':
                cnt += 1
            else:
                copied += s[idx]
            idx +=1
        s = ''
        m = len(copied)
        
        while m > 0:
            s = str(m % 2) + s
            m //= 2
        

    return [turn, cnt]

s = "110010101001"
print(solution(s))