import sys
input = sys.stdin.readline

n = int(input().strip())
coordinate = []
coordinate.append((0,0))
for _ in range(n):
    coordinate.append(list(map(int, input().split())))

d = {}

for i, coord1 in enumerate(coordinate):
    neighbors = []
    for j, coord2 in enumerate(coordinate):
        if i != j:  # 자신과는 비교하지 않음
            # 첫 번째 값이나 두 번째 값이 같은 경우를 이웃으로 간주
            if coord1[0] == coord2[0] or coord1[1] == coord2[1]:
                neighbors.append(tuple(coord2))
    d[tuple(coord1)] = neighbors

start = (0,0)

count = 0
def backtrack(d, start, path):
    global count
    for value in d[start]:
        if len(path) == len(d) and (0, 0) in d[path[-1]] :
            count += 1
            return
        if value in path:
            continue 
        if len(path) == len(d) and [path][-1] != (0, 0):
            return
        path.append(value)
        backtrack(d, value, path)
        path.pop()

backtrack(d, start, [start])
print(count)