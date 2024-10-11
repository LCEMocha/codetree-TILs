K = int(input())
graph = [[False for _ in range(5)] for _ in range(5)]
count = 0

for _ in range(K):
    y, x = map(int, input().split())
    graph[y-1][x-1] = 'x'

'''
graph = [
    [True, True, True, False, False],
    [True, True, True, False, False],
    ['x', 'x', 'x', 'x', False],
    [True, True, True, False, False],
    [True, True, True, False, False]
]
'''

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def try_move(current_y, current_x):
    global dx, dy, graph

    moves = []
    for i in range(4):
        next_x = current_x + dx[i]
        next_y = current_y + dy[i]
        
        if (0 <= next_x < len(graph)) and (0 <= next_y < len(graph)):  
            if graph[next_y][next_x] != 'x' and not graph[next_y][next_x]:  
                moves.append((next_y, next_x))  # 모든 가능한 이동을 리스트에 추가
    return moves


def backtrack(current_Ay, current_Ax, current_By, current_Bx):
    global graph, count, K

    graph[current_Ay][current_Ax] = True
    graph[current_By][current_Bx] = True

    possible_A_moves = try_move(current_Ay, current_Ax)
    # possible_A_moves가 존재한다면 A의 모든 가능한 이동을 시도
    if possible_A_moves:   
        for next_Ay, next_Ax in possible_A_moves:
            # possible_B_moves가 존재한다면 B의 모든 가능한 이동을 시도
            possible_B_moves = try_move(current_By, current_Bx) 
            if possible_B_moves:
                for next_By, next_Bx in possible_B_moves:
                    if (next_Ax == next_Bx) and (next_Ay == next_By):
                        # A, B가 모든 칸을 탐색하고 최종적으로 같은 칸을 밟는 경우
                        if (sum(row.count(True) for row in graph) == 24-K):
                            count += 1
                    else:
                        backtrack(next_Ay, next_Ax, next_By, next_Bx)
    graph[current_Ay][current_Ax] = False
    graph[current_By][current_Bx] = False


backtrack(0, 0, 4, 4)
print(count)