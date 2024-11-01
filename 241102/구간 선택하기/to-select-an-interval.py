import sys

n = int(input())

intervals = []
for line in sys.stdin:
    a, b = map(int, line.split())
    intervals.append([a, b])

n = len(intervals)

def min_intervals_to_cover(intervals):
    # 구간을 시작점 기준으로 오름차순, 끝점 기준으로 내림차순 정렬
    intervals.sort(key=lambda x: (x[0], -x[1]))

    # 덮고자 하는 구간의 시작과 끝
    target_start, target_end = 3, 220
    current_end = target_start
    max_reach = target_start
    count = 0
    i = 0

    while i < n and current_end < target_end:
        # 현재 범위 내에서 가장 멀리 덮을 수 있는 구간을 찾음
        while i < n and intervals[i][0] <= current_end:
            max_reach = max(max_reach, intervals[i][1])
            i += 1
        
        # 덮을 수 있는 최대 범위가 늘어나지 않으면 덮을 수 없는 경우
        if max_reach == current_end:
            return 0
        
        # 구간 선택 후 현재 끝 범위 갱신
        current_end = max_reach
        count += 1
    
    # 끝까지 덮었는지 확인
    if current_end >= target_end:
        return count
    else:
        return 0

print(min_intervals_to_cover(intervals))