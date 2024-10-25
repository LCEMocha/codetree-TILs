import sys
from collections import deque
input = sys.stdin.readline

N = int(input().strip())
blocks = []
for i in range(N):
    r, c = map(int, input().split())
    blocks.append([r,c])


def calculate_perimeter(N, blocks):
    # 100 x 100 크기의 격자 생성
    grid = [[0] * 102 for _ in range(102)]
    
    # 블록 위치 표시
    for r, c in blocks:
        grid[r][c] = 1
    
    # 외부 빈 공간 찾기 (Flood Fill)
    queue = deque([(0, 0)])
    visited = [[False] * 102 for _ in range(102)]
    visited[0][0] = True
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상, 하, 좌, 우
    
    while queue:
        r, c = queue.popleft()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < 102 and 0 <= nc < 102 and not visited[nr][nc] and grid[nr][nc] == 0:
                visited[nr][nc] = True
                queue.append((nr, nc))
    
    # 둘레 계산
    perimeter = 0
    for r, c in blocks:
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            # 외부와 연결된 빈 공간에만 둘레로 간주
            if visited[nr][nc]:
                perimeter += 1
    
    return perimeter


# 함수 호출 및 결과 출력
print(calculate_perimeter(N, blocks))