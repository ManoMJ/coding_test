def solution(arr):
    min_idx=0
    mn=arr[0]
    for idx, n in enumerate(arr):
        if n < mn:
            mn=n
            min_idx=idx
    del arr[min_idx]
    if len(arr)==0:
        return [-1]
    return arr