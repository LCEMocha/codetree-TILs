n = int(input())  
numbers = {}

for i in range(1, n + 1):
    numbers[i] = int(input())

is_loop = [False] * (n + 1) 
count = 0

def dfs(k, current_visit):
    if k == 0:
        return
    current_visit.append(k)
    if numbers[k] in current_visit or is_loop[k]:
        loop = [k]
        while loop :
            next_val = loop.pop()
            if is_loop[next_val]:
                continue
            is_loop[next_val] = True
            node = [k for k, v in numbers.items() if v == next_val]
            #print(next_val, loop, node, is_loop)
            if node:
                for i in node:
                    loop.append(i)
                    #print(loop)
    else:
        dfs(numbers[k], current_visit)
                        

for i in range(1, n+1):
    dfs(i, [])

print(is_loop[1:].count(False))