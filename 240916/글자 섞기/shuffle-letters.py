N = int(input())
first = []
last = []

# 단어와 인덱스를 묶음
for i in range(N):
    s = str(input())
    sorted_s = sorted(s)
    first.append([sorted_s[0]])
    p = sorted_s.pop()
    last.append([p])

sorted_first = sorted(first)
sorted_last = sorted(last)

# 빠른순서 찾기
for i in range(len(first)):
    append_flag = True
    for j in range(len(last)):
        if first[i][0] <= sorted_last[0][0]:
            first[i].append(0)
            append_flag = False
            break
        if (j+1<len(last)) and (first[i][0] >= sorted_last[j][0]) and (first[i][0] <= sorted_last[j+1][0]):
            first[i].append(j+1)
            append_flag = False
            break
        append_flag = True
    if append_flag:
        first[i].append(len(last)-1)


# 느린순서 찾기
for i in range(len(last)):
    append_flag = True
    for j in range(len(sorted_first)):
        if last[i][0] <= sorted_first[0][0]:
            last[i].append(0)
            append_flag = False
            break
        if (j+1<len(last)) and (sorted_first[j][0] <= last[i][0]) and (sorted_first[j+1][0] >= last[i][0]):
            last[i].append(j)
            append_flag = False
            break
        append_flag = True
    if append_flag:
        last[i].append(len(last)-1)


for i in range(len(first)):
    print(first[i][1]+1, last[i][1]+1)