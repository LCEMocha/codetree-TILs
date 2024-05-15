def find_cycles_and_max_cycle_size(n, initial, target):
  
    initial_to_target = {initial[i]: target[i] for i in range(n)}
    
    visited = [False] * (n + 1)
    cycle_count = 0
    max_cycle_size = 0


    def dfs(node):
        cycle_size = 0
        current = node
        while not visited[current]:
            visited[current] = True
            current = initial_to_target[current]
            cycle_size += 1
        return cycle_size
    

    for i in range(1, n + 1):
        if not visited[i]:
            cycle_size = dfs(i)
            if cycle_size > 0:
                cycle_count += 1
                max_cycle_size = max(max_cycle_size, cycle_size)
    
    return cycle_count, max_cycle_size


n = int(input())
initial = [int(input()) for _ in range(n)]
target = [int(input()) for _ in range(n)]

cycle_count, max_cycle_size = find_cycles_and_max_cycle_size(n, initial, target)

print(cycle_count, max_cycle_size)