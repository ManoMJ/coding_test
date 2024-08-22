def solution(s):
    arr = list(map(int, s.split()))
    mx, mn = max(arr), min(arr)
    answer = str(mn) + ' ' + str(mx)
    
    return answer

print(solution('1 2 3 4'))