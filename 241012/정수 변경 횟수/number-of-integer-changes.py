N, K, M = map(int, input().split())
num_list = list(map(int, input().split()))
max_calculate = -1
dp = {}

def backtrack(cur_calculate, n, i):
    global max_calculate

    if n == N:
        max_calculate = max(max_calculate, cur_calculate)
        return
    
    # 현재 상태가 이미 방문한 상태라면 return
    if (cur_calculate, n, i) in dp:
        return

    dp[(cur_calculate, n, i)] = True  # 현재 상태를 방문한 것으로 기록

    if n < N:  
        # 더하는 경우
        if cur_calculate + num_list[i] <= M:
            backtrack(cur_calculate + num_list[i], n + 1, i + 1)
        # 빼는 경우
        if cur_calculate - num_list[i] >= 0:
            backtrack(cur_calculate - num_list[i], n + 1, i + 1)

# 백트래킹 시작
backtrack(K, 0, 0)
print(max_calculate)