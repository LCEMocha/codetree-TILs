# 입력 받기
n = int(input())
papers = [list(map(int, input().split())) for _ in range(n)]

# 색종이가 붙여질 2차원 그리드 초기화
grid = [[0] * 101 for _ in range(101)]

for x, y in papers:
    for i in range(x, x+10):
        for j in range(y, y+10):
            grid[i][j] = 1

perimeter = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(101):
    for j in range(101):
        if grid[i][j] == 1:
            for d in range(4):
                if grid[i+dx[d]][j+dy[d]] == 0:
                    perimeter += 1

print(perimeter)