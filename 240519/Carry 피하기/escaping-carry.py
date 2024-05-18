N = int(input())
nums = []

for _ in range(N):
    n = int(input())
    nums.append(n)

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

def backtrack(current_sum, depth, count):
    global nums
    global max_count
    max_count = max(count, max_count)
    for i in range(depth, len(nums)):
        if is_not_carry(current_sum, nums[i]):
            current_sum += nums[i]
            backtrack(current_sum, i+1, count+1)

backtrack(0, 0, 0)

print(max_count)