N = int(input())
max_len = 0
grid = []

for i in range(N):
    row = list(input().strip())
    grid.append(row)

visited = [[False for _ in range(N)] for _ in range(N)]

def backtrack(grid, N, visited, curr_len, x, y, open_count, close_count):
    global max_len
    visited[x][y] = True

    # 괄호 수가 일치하지 않으면 더 이상 진행하지 않음
    if close_count > open_count:
        visited[x][y] = False
        return

    # 괄호 수가 일치하고, 경로가 유효한 경우 최대 길이 갱신
    if open_count == close_count:
        max_len = max(max_len, curr_len)

    # 다음 가능한 경로로 이동
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
            # 이전 위치가 ')'이고, 다음 위치가 '('인 경우 이동하지 않음   
            if not (grid[x][y] == ')' and grid[nx][ny] == '('):            
                if grid[nx][ny] == '(':
                    backtrack(grid, N, visited, curr_len + 1, nx, ny, open_count + 1, close_count)
                elif grid[nx][ny] == ')':                               
                    backtrack(grid, N, visited, curr_len + 1, nx, ny, open_count, close_count + 1)

    visited[x][y] = False  # 상태 복구

backtrack(grid, N, visited, 1, 0, 0, 1, 0)

print(max_len)