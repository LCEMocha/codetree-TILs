from collections import defaultdict
import copy

n = int(input())
numbers = defaultdict(list)
count = 0

for i in range(n):
    numbers[i+1].append(int(input()))

def dfs(k, current_count, copy_numberes, current_visit):
    global count
    global flag
    current_visit.append(k)
    if copy_numberes[k]:  
        next_value = copy_numberes[k].pop()
        if next_value == 0 and current_count == 0:
            flag = False
            return flag
        if next_value in current_visit:
            flag = False
            return flag
        if next_value == 0 or not copy_numberes[next_value]:
            count += (current_count + 1)
            flag = False
            return flag
        if next_value != 0 and next_value not in current_visit:
            dfs(next_value, current_count+1, copy_numberes, current_visit)


for k in numbers.keys():
    flag = True
    copy_numbers = copy.deepcopy(numbers)
    while flag :
        dfs(k, 0, copy_numbers, [])
    
print(count)