def solution(n):
    if n <= 1:
        return n

    MOD = 1234567
    fibo = [0] * (n + 1)
    fibo[1] = 1

    for i in range(2, n + 1):
        fibo[i] = (fibo[i-1] + fibo[i-2]) % MOD

    return fibo[n]

# 테스트
print(solution(10))  # 55 % 1234567 = 55
print(solution(20))  # 6765 % 1234567 = 6765
print(solution(30))  # 832040 % 1234567 = 832040
