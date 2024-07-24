def solution(numbers, target):
    answer =[0]
    
    def dfs(idx, cur) :
        if idx == len(numbers):
            if cur == target:
                answer[0] += 1
            return None
        dfs(idx + 1, cur + numbers[idx])
        dfs(idx + 1, cur - numbers[idx])
        
    
    dfs(0, 0)
    return answer[0]

numbers = [1, 1, 1, 1, 1]
target = 3
solution(numbers, target)