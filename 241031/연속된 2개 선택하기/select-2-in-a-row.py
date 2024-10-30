import sys
input = sys.stdin.readline

n = int(input().strip())
list_n = []

for _ in range(n):
    list_n.extend(list(map(int, input().split())))

def max_sum_no_three_consecutive(arr):
    if n == 0:
        return 0
    elif n == 1:
        return arr[0]
    elif n == 2:
        return arr[0] + arr[1]

    dp = [0] * n
    dp[0] = arr[0]
    dp[1] = arr[0] + arr[1]
    dp[2] = max(arr[0] + arr[1], arr[1] + arr[2], arr[0] + arr[2])

    for i in range(3, n):
        # dp[i-1]: 현재 위치 i의 수를 선택하지 않는 경우
        # dp[i-2] + arr[i]: 현재 위치 i의 수만 선택하는 경우
        # dp[i-3] + arr[i-1] + arr[i]: 현재 위치 i와 이전 위치 i-1의 수를 선택하는 경우
        dp[i] = max(dp[i-1], dp[i-2] + arr[i], dp[i-3] + arr[i-1] + arr[i])

    return dp[-1]


print(max_sum_no_three_consecutive(list_n))