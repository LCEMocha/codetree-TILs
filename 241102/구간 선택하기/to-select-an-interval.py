import sys
input = sys.stdin.readline

n = int(input().strip())

coverage = []
for _ in range(n):
    coverage.append(list(map(int, input().split())))

coverage = sorted(coverage, key=lambda x: (x[1], x[1] - x[0]), reverse=True)

for i in range(len(coverage)):
    if coverage[i][1]<=3 or 221<coverage[i][0]:
        coverage.pop(i)

count = 1
current_a, current_b = coverage[0][0], coverage[0][1]
coverage_left = current_a - 2
current_end = coverage[0][1]
current_start = coverage[0][0]
for a, b in coverage:
    current_left = a - 2
    print("a:", a, "b:", b, coverage_left, current_left, current_a, current_b)
    if (a < current_a) and (current_a <= b < current_b) and coverage_left > current_left:
        coverage_left = current_left
        current_a, current_b = a, b
        current_start = a
        count += 1

if current_a > 221:
    print(0)
elif current_start > 3 or current_end <= 220:
    print(0)
else:
    print(count)