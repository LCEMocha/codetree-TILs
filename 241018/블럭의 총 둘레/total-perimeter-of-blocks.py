import sys
input = sys.stdin.readline
from collections import deque

n = int(input().strip())
blocks = []
for _ in range(n):
    blocks.append(list(map(int, input().split())))

# 상하좌우 네 방향에 대한 이동 좌표
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def flood_fill(grid, start_x, start_y):
    queue = deque([(start_x, start_y)])
    visited = set()
    visited.add((start_x, start_y))
    
    while queue:
        x, y = queue.popleft()
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 100 and 0 <= ny < 100 and (nx, ny) not in visited and not grid[nx][ny]:
                visited.add((nx, ny))
                queue.append((nx, ny))
    
    return visited

def calculate_perimeter(blocks):
    # 100x100 좌표계를 모두 False로 초기화 (블록이 없는 곳은 False)
    grid = [[False] * 100 for _ in range(100)]

    # 입력된 블록들의 위치를 표시
    for x, y in blocks:
        grid[x-1][y-1] = True

    # 외부와 연결된 빈 공간을 탐색 (좌상단에서 시작)
    external_space = flood_fill(grid, 0, 0)

    perimeter = 0

    # 각 블록에 대해 외부로 노출된 면을 계산
    for x, y in blocks:
        x, y = x - 1, y - 1
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            # 범위를 벗어나거나, 인접한 곳이 외부 공간인 경우 둘레로 간주
            if nx < 0 or ny < 0 or nx >= 100 or ny >= 100 or (nx, ny) in external_space:
                perimeter += 1

    return perimeter

result = calculate_perimeter(blocks)
print(result)