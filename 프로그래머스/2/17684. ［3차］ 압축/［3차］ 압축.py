def get_dict():
    dict= {}
    cnt=1
    for char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        dict[char] = cnt
        cnt+=1
    return dict, cnt

def solution(msg):
    answer = []
    dict, last_index = get_dict()
    index=0
    while index < len(msg):
        key = msg[index]
        original_key = key
        cnt = index+1
        while key in dict and cnt < len(msg):
            original_key = key
            key += msg[cnt]
            cnt += 1
        if key in dict:
            original_key = key
        answer.append(dict[original_key])
        dict[key] = last_index
        last_index += 1
        index+= len(original_key)
    return answer
        

msg = "KAKAO"
print(solution(msg))