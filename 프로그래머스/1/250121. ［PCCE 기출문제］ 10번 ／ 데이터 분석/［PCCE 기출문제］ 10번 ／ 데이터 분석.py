def solution(data, ext, val_ext, sort_by):
    answer = []
    if ext=="code":
            idx = 0
    elif ext=="date":
        idx = 1
    elif ext=="maximum":
        idx = 2
    elif ext=="remain":
        idx = 3

    if sort_by=="code":
        sorti = 0
    elif sort_by=="date":
        sorti = 1
    elif sort_by=="maximum":
        sorti = 2
    elif sort_by=="remain":
        sorti = 3

    for d in data:
        if d[idx] < int(val_ext):
             answer.append(d)
    
    answer.sort(key=lambda x:x[sorti])
        
    return answer

data = [[1, 20300104, 100, 80], [2, 20300804, 847, 37], [3, 20300401, 10, 8]]
ext = "date"
val_ext = "20300501"
sort_by = "remain"
print(solution(data, ext, val_ext, sort_by))