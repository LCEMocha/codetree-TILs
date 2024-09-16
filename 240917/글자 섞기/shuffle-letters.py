import bisect

N = int(input())
first = []
last = []

for i in range(N):
    s = input().strip()
    sorted_s = ''.join(sorted(s))
    reverse_s = ''.join(sorted_s[::-1])
    first.append([sorted_s, i])  
    last.append([reverse_s, i])

first.sort()
last.sort()

first_positions = [0] * N
last_positions = [0] * N

# 이진탐색
for i in range(N):
    # 빠른순서 정렬
    first_positions[first[i][1]] = bisect.bisect_left([x[0] for x in last], first[i][0])
    # 느린 순서 정렬
    last_positions[last[i][1]] = bisect.bisect_right([x[0] for x in first], last[i][0])

for i in range(N):
    print(first_positions[i] + 1, last_positions[i])