def solution(A, B):
    answer = 0
    n = len(B)
    A.sort(reverse=True)
    B.sort(reverse=True)
    bi = ai = 0
    while ai < n:
        if A[ai] < B[bi]:
            bi += 1
            answer +=1
        ai += 1
    return answer
