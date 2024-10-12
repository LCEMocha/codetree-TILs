N, K, M = map(int, input().split())
num_list = list(map(int, input().split()))
max_calculate = -1
dp = {}

def backtrack(cur_calculate, n):
    global max_calculate

    if n == N :
        max_calculate = max(max_calculate, cur_calculate)
        return
    
    if (cur_calculate, n) in dp:
        return

    elif n < N:
        for i in num_list:
            if cur_calculate + i < M:
                dp[(cur_calculate, n)] = max_calculate               
                backtrack(cur_calculate + i, n+1)
                
            if cur_calculate - i >= 0:
                dp[(cur_calculate, n)] = max_calculate
                backtrack(cur_calculate - i, n+1)   

    else:
        dp[(cur_calculate, n)] = max_calculate
        return -1

backtrack(K, 0)
print(max_calculate)