def solution(citations):
    citations.sort(reverse=True)
    for i, c in enumerate(citations):
        if i + 1 > c:
            return i
    return len(citations)

print(solution([3, 0, 6, 1, 5]))