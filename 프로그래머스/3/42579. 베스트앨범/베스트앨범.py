from collections import defaultdict

def solution(genres, plays):
    hash_ = defaultdict(list)
    
    for i in range(len(genres)):
        hash_[genres[i]].append([plays[i], i])
    
    sums = []

    for k, v in hash_.items():
        v.sort(key=lambda x : -x[0])
        sums.append((k, sum(i[0] for i in v)))
    
    sums.sort(key = lambda x : -x[1])

    playlist = defaultdict(list)
    for k, v in hash_.items():
        playlist[k].append(v[0][1])
        if len(v) > 1:
            playlist[k].append(v[1][1])

    print(playlist)
    answer = []
    for c, s in sums:
        li = playlist.get(c)
        answer += li
    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))