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
            dp[(cur_calculate, n)] = max_calculate
            if cur_calculate + i <= M:               
                backtrack(cur_calculate + i, n+1)
                #dp[(cur_calculate, n)] = max_calculate
                
            if cur_calculate - i >= 0:             
                backtrack(cur_calculate - i, n+1)
                #dp[(cur_calculate, n)] = max_calculate 

    else:
        dp[(cur_calculate, n)] = max_calculate
        return -1

backtrack(K, 1)
print(max_calculate)