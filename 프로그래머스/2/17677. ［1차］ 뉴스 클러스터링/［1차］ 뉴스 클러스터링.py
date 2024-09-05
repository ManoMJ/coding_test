import re
from collections import Counter

def solution(str1, str2):
    answer = 0
    str1 = str1.lower()
    str2 = str2.lower()
    subset1 = []
    subset2 = []
    for i in range(len(str1)-1):
        new_word = str1[i:i+2]
        if re.match("[a-z]{2}", new_word):
            subset1.append(new_word)
    for i in range(len(str2)-1):
        new_word = str2[i:i+2]
        if re.match("[a-z]{2}", new_word):
            subset2.append(new_word)
    counter1 = Counter(subset1)
    counter2 = Counter(subset2)
    # 교집합과 합집합 계산
    intersection = sum((counter1 & counter2).values())  # &는 교집합의 최소 개수
    union = sum((counter1 | counter2).values())         # |는 합집합의 최대 개수
    
    # 자카드 유사도 계산
    if union == 0:  # 두 집합이 모두 공집합일 경우
        return 65536
    else:
        answer = int((intersection / union) * 65536)
        return answer