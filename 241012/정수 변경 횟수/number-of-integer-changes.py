N, K, M = map(int, input().split())
num_list = list(map(int, input().split()))
max_calculate = K

def backtrack(cur_calculate, n):
    global max_calculate

    if n == N :
        max_calculate = max(max_calculate, cur_calculate)
        return
    
    elif n < N:
        for i in num_list:
            if cur_calculate + i < M:
                backtrack(cur_calculate + i, n+1)
            if cur_calculate - i >= 0:
                backtrack(cur_calculate - i, n+1)
    
    else:
        return -1

if backtrack(K, 1) == -1:
    print(-1)
else:
    print(max_calculate)