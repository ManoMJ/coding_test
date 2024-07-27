def solution(s):
    def iter(sub_s):
        stack = []
        for char in sub_s:
            if char=='[' or char=='(' or char=='{':
                stack.append(char)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if top=='[' and char!=']':
                    return False
                elif top=='{' and char!='}':
                    return False
                elif top=='(' and char!=')':
                    return False
        if not stack:
            return True
    answer = 0
    double_s = s * 2
    for i in range(len(s)):
        sub_s = double_s[i:i+len(s)]
        
        if iter(sub_s):
            answer += 1
    return answer

print(solution("}]()[{"))
