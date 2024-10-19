def solution(brown, yellow):
    total_tiles = brown + yellow  # 전체 격자 수
    
    # 가능한 가로, 세로 조합을 찾습니다
    for height in range(3, int(total_tiles**0.5) + 1):
        if total_tiles % height == 0:  # 나눠떨어지면 가능한 가로, 세로 쌍
            width = total_tiles // height
            # 갈색과 노란색 개수가 조건을 만족하는지 확인
            if brown == (2 * width + 2 * height - 4) and yellow == (width - 2) * (height - 2):
                return [width, height]

# 테스트 실행
print(solution(10, 2))  # [4, 3]
print(solution(8, 1))   # [3, 3]
print(solution(24, 24)) # [8, 6]
