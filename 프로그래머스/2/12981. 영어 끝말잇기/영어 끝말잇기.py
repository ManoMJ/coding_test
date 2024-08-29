def solution(n, words):
    answer = []
    memo = {}
    prev = words[0]
    memo[prev] = 0
    for i in range(1, len(words)):
        word = words[i]
        if word[0] != prev[-1] or word in memo:
            idx = i % n + 1
            turn = i // n + 1
            return [idx, turn]
        memo[word] = 0
        prev = word
        
    return [0, 0]