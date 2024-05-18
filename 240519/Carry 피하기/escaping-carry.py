N = int(input())
nums = [int(input().strip()) for _ in range(N)]

max_count = 0

def is_not_carry(sum, target):
    # sum 또는 target의 자릿수를 모두 사용할 때까지 반복
    while sum > 0 or target > 0:
        num1 = sum % 10
        num2 = target % 10

        # 현재 자릿수들의 합이 carry가 발생하는지 확인
        if num1 + num2 >= 10:
            return False

        # 다음 자릿수 합 비교
        sum //= 10
        target //= 10

    # 반복문이 정상으로 종료되면 carry가 발생하지 않음
    return True

def backtrack(count, depth, sum):
    global max_count

    # 이전까지 최대 개수(max_count)와 현재까지 구한 개수(count) 중 큰 값으로 갱신
    max_count = max(max_count, count)

    # nums 순회
    for i in range(depth, N):
        # carry가 발생하지 않았다면
        if is_not_carry(sum, nums[i]):
            # count, depth 증가시키고, sum과 nums[i]를 더한 후 backtrack 재귀 호출
            backtrack(count + 1, i + 1, sum + nums[i])

# 초기 백트래킹 시작
backtrack(0, 0, 0)
print(max_count)