def solution(routes):
    routes.sort(key=lambda x: x[1]) 
    cameras = []
    camera_count = 0

    for route in routes:
        start, end = route
        if not cameras or cameras[-1] < start:
            cameras.append(end)
            camera_count += 1

    return camera_count
 
