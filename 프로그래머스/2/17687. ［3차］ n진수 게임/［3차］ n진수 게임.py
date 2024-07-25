def solution(n, t, m, p):
    answer = ''
    index = 0
    number = 0
    while len(answer) < t:
        res = convert_to_base(number, n)
        for char in res:
            if len(answer) >= t:
                break
            if index % m == p - 1:
                answer += char
            index += 1
        number += 1
    return answer

def convert_to_base(num, base):
    chars = "0123456789ABCDEF"
    if num == 0:
        return "0"
    result = ""
    while num > 0:
        result = chars[num % base] + result
        num //= base
    return result

r = solution(2, 4, 2, 1)
print(r)