N = int(input())
max_len = 0
curr_len = 0
grid = []

for i in range(N):
    row = list(input().strip())
    grid.append(row)

visited = [[False for _ in range(N)] for _ in range(N)]

def is_visited(x, y, grid, N):
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if (0 <= nx < N and 0 <= ny < N) and (not visited[nx][ny]) and (grid[nx][ny] == ')'):
            return False  # 하나라도 조건을 만족하지 않으면 False 반환   
    return True  # 모든 조건을 만족하면 True 반환

def backtrack(grid, N, visited, curr_len, x, y):
    global max_len
    visited[x][y] = True

    if (0 <= x < N and 0 <= y < N) and (grid[x][y] == ')') and is_visited(x, y, grid, N):
        max_len = max(max_len, curr_len)
        visited[x][y] = False
        return 

    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
            # grid[x][y]가 ')'이고, grid[nx][ny]가 '('이면 이동하지 않음
            if not (grid[x][y] == ')' and grid[nx][ny] == '('):
                backtrack(grid, N, visited, curr_len + 1, nx, ny)
    visited[x][y] = False  # 상태 복구

backtrack(grid, N, visited, 1, 0, 0)

print(max_len)