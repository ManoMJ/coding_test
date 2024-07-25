def conver_to_base(num, n):
    if num == 0:
        return '0'
    if n==10:
        return str(num)
    result = ''
    while num > 0:
        result = str(num % n) + result
        num  //= n
    return result
def solution(n, k):
    num = conver_to_base(n, k).split('0')
    #print(num)
    answer = 0
    for i in range(len(num)):
        if num[i] and is_prime(int(num[i])):
            answer += 1

    return answer
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5)+1):
        if n % i == 0:
            return False
    return True

print(solution(110011, 10))
print(conver_to_base(5, 3))