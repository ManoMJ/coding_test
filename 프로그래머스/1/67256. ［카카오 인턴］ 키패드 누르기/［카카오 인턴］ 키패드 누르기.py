phone = {
    1: (0, 0),
    2: (0, 1),
    3: (0, 2),
    4: (1, 0),
    5: (1, 1),
    6: (1, 2),
    7: (2, 0),
    8: (2, 1),
    9: (2, 2),
    10: (3, 0),
    0: (3, 1),
    11: (3, 2)
}
def solution(numbers, hand):
    answer = ''
    prev_l = 10
    prev_r = 11
    for i, n in enumerate(numbers):
        if n in [1, 4, 7]:
            answer += "L"
            prev_l = n
        elif n in [3, 6, 9]:
            answer += "R"
            prev_r = n
        else:
            ld = abs(phone[prev_l][0] - phone[n][0]) + abs(phone[prev_l][1] - phone[n][1])
            rd = abs(phone[prev_r][0] - phone[n][0]) + abs(phone[prev_r][1] - phone[n][1])
            if ld > rd or (ld==rd and hand=="right"):
                prev_r = n
                answer += "R"
            else :
                prev_l = n
                answer += "L"
                
            
    return answer

numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]	
hand = "right"
print(solution(numbers, hand))