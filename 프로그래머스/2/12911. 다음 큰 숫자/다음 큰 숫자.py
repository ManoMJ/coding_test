def solution(n):
    count_ones = bin(n).count('1')
    
    while True:
        n += 1
        if bin(n).count('1') == count_ones:
            return n
