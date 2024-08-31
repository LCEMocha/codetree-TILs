N = int(input())
numbers = [int(input()) for _ in range(N)]
deDuplicate = list(set(numbers))
max_continue = [1, 0]

for i in deDuplicate:
    filtered_numbers = [x for x in numbers if x != i]
    if not filtered_numbers:
        max_continue = [0, 0]
    curr_continue = [[0, 0] for _ in range(len(deDuplicate))]
    curr_continue_count = 0
    for j in range(len(filtered_numbers)):       
        if j+1<=len(filtered_numbers)-1 and filtered_numbers[j] == filtered_numbers[j+1]:
            curr_continue_count += 1
        elif j>0 and filtered_numbers[j] == filtered_numbers[j-1]:
            curr_continue_count += 1
            index = deDuplicate.index(filtered_numbers[j]) 
            if curr_continue[index][0] < curr_continue_count:
                curr_continue[index][1] = [filtered_numbers[j]]
                curr_continue[index][0] = curr_continue_count
        else:
            curr_continue_count = 0
            continue
   
    max_curr = max(curr_continue)
    max_continue = max(max_continue, max_curr)

print(max_continue[0])