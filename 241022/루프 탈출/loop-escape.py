n = int(input())  
numbers = {}

for i in range(1, n + 1):
    numbers[i] = int(input())

visited = [False] * (n + 1) 
#print(numbers)
count = 0
def dfs(k, current_count):
    global visited
    global count
    visited[k] = True
    next_val = numbers[k]
    #print("nv: ", next_val, visited, current_count, "카운트:",count)
    if next_val == 0:
        count += current_count
        return
    if visited[next_val] == True and numbers[next_val] != 0:
        return
    if visited[next_val] == False and numbers[next_val] != 0:
        dfs(next_val, current_count+1)
    if visited[next_val] == False and numbers[next_val] == 0:
        count += current_count + 1
        visited[next_val] = True
        return
    if visited[next_val] == True and numbers[next_val] == 0:
        count += current_count
        return

for i in range(1, n + 1):
    dfs(i, 1)

print(count)