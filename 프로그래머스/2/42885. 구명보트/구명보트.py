from collections import deque

def solution(people, limit):
    answer = 0
    people.sort()
    people = deque(people)
    while people:
        heavy = people.pop()
        cur = [heavy]
        
        if people and heavy + people[0] <= limit:
            cur.append(people.popleft())
        
        answer += 1
    return answer