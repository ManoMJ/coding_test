def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []
    
    for idx in range(len(numbers)-1, -1, -1):
        while stack and stack[-1] <= numbers[idx]:
            stack.pop()
        if stack:
            answer[idx] = stack[-1]
        stack.append(numbers[idx])
            
    return answer