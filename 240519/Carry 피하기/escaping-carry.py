N = int(input())
nums = []

for _ in range(N):
    n = str(input())
    nums.append(n)

max_count = 0

def backtrack(current_results):
    global nums, max_count
    if len(current_results) >= 2:
        max_len = max(len(num) for num in current_results)
        # 모든 숫자의 자릿수를 맞추기 위해 앞에 '0'을 추가
        str_numbers = [num.zfill(max_len) for num in current_results]

        # 각 자릿수를 더하기 위해 자릿수별로 분할
        digit_sums = [sum(int(num[i]) for num in str_numbers) for i in range(max_len)]

        if any(digit_sum >= 10 for digit_sum in digit_sums):
            return
        else:
            max_count = max(max_count, len(current_results))

    for i in range(len(nums)):
        backtrack(current_results + [nums[i]])

backtrack([])

print(max_count)