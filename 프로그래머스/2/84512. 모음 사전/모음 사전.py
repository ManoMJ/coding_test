def solution(word):
    vowels = ['A', 'E', 'I', 'O', 'U']
    position = {v: i+1 for i, v in enumerate(vowels)}
    
    # 각 자리의 가중치
    weights = [781, 156, 31, 6, 1]
    
    total = 0
    
    for i, char in enumerate(word):
        total += (position[char] - 1) * weights[i] + 1
        
    return total

