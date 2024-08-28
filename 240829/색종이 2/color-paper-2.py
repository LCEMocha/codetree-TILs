# 입력 받기
n = int(input())
papers = [tuple(map(int, input().split())) for _ in range(n)]

# 색종이가 붙여질 2차원 그리드 초기화
grid = [[0] * 101 for _ in range(101)]

# 색종이 영역을 그리드에 표시
for x, y in papers:
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            grid[i][j] = 1

# 둘레 계산
perimeter = 0
dx = [0, 0, -1, 1]  # 상, 하, 좌, 우
dy = [1, -1, 0, 0]  # 상, 하, 좌, 우

for i in range(101):
    for j in range(101):
        if grid[i][j] == 1:  # 색종이가 붙어 있는 영역이라면
            for k in range(4):  # 상, 하, 좌, 우 네 방향을 확인
                ni, nj = i + dx[k], j + dy[k]
                # 인접한 칸이 색종이가 없는 영역이면 둘레에 포함
                if grid[ni][nj] == 0:
                    perimeter += 1

# 결과 출력
print(perimeter)