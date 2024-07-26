def solution(elements):
    n = len(elements)
    circular_elements = elements * 2  # 원형 수열 만들기 위해 두 번 이어붙임
    sums = set()  # 부분 수열의 합을 저장할 집합

    # 모든 길이의 부분 수열을 구함
    for length in range(1, n + 1):
        for start in range(n):
            sub_sum = sum(circular_elements[start:start + length])
            sums.add(sub_sum)
    
    return len(sums)

# 예제 테스트 케이스
print(solution([7, 9, 1, 1, 4]))  # 예상 결과: 18
