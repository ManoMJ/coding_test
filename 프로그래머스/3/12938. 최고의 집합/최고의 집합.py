
def solution(n, s):
    if s<n:
        return [-1]
    
    mid = s//n
    r = s % n 

    a = [mid] * n
    for i in range(r):
        a[i] += 1
    a.sort()
    return a

print(solution(3,8))