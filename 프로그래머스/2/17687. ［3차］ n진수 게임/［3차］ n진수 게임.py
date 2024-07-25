def solution(n, t, m, p):
    answer = ''
    index=1
    cur=0
    while len(answer) < t:
        res = make_n(n, cur)
        for i in range(len(res)):
            if len(answer) >= t:
                break
            if index%m==p or (index%p==0 and m==p):
                answer += res[i]
            index+=1
        cur+=1
    return answer

cor = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
def make_n(n, number):
    if not number:
        return '0'
    result = ''
    while number > 1:
        mod = number % n
        if mod >= 10:
            mod = cor[mod]
        result = str(mod) + result
        number = number // n
    if number:
        result = str(number) + result
    return result

r = solution(2, 4, 2, 1)
print(r)