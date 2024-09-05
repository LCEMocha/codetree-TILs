N = int(input())
first = []
last = []
for i in range(N):
    s = str(input())
    sorted_s = sorted(s)
    p = sorted_s.pop()
    first.append([sorted_s[0], i])
    last.append([p, i])

sorted(first)
sorted(last)
for i in first:
    idx = first.index(i)
    first[i].append(idx)
print(first)