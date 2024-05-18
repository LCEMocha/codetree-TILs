N = int(input())
nums = [input().strip() for _ in range(N)]

# 전역 변수 선언
max_count = 0

# 메모이제이션을 위한 딕셔너리
memo = {}

def can_add(current_results, new_number):
    # 새로운 숫자를 더했을 때 자릿수의 합이 10을 넘지 않는지 확인
    max_len = max(len(num) for num in current_results + [new_number])
    str_numbers = [num.zfill(max_len) for num in current_results] + [new_number.zfill(max_len)]
    
    for i in range(max_len):
        if sum(int(num[i]) for num in str_numbers) >= 10:
            return False
    return True

def backtrack(current_results, index):
    global max_count
    
    # 메모이제이션 체크
    state = (tuple(current_results), index)
    if state in memo:
        return memo[state]
    
    if len(current_results) >= 2:
        max_count = max(max_count, len(current_results))
    
    for i in range(index, N):
        if can_add(current_results, nums[i]):
            backtrack(current_results + [nums[i]], i + 1)
    
    # 메모이제이션 저장
    memo[state] = max_count

backtrack([], 0)
print(max_count)