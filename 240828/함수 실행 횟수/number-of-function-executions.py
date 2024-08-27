n = int(input())

# 메모이제이션을 위한 배열 초기화
memo = [-1] * (n + 1)

def count(N):
    if N == 0 or N == 1:
        return 1
    if N == 2:
        return 3
    if N == 3:
        return 5
    if memo[N] != -1:
        return memo[N]  # 이미 계산된 값이 있으면 그 값을 반환
    else:
        # 값을 계산하고 메모 배열에 저장
        memo[N] = count(N-1) + count(N-2) + 1
        return memo[N]

print(count(n)%1000000007)