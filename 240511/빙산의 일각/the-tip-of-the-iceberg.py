N = int(input())
iceburg = []
for _ in range(N):
    i = int(input())
    iceburg.append(i)

if N <= 2:
    if iceburg == [1, 1]:
        print(0)
    else:
        print(1)

iceburg_sorted = sorted(list(enumerate(iceburg)))
mid = iceburg[int(len(iceburg) // 2)]
idx = [idx for idx, value in iceburg_sorted if value == mid][0]
idxs = [2]

result = []
for i in idxs:
    count = 0
    for ice in range(0, len(iceburg), 2):
        # 전 얼음이 해수면보다 높고 현 얼음이 해수면과 같거나 작으면 count+1
        if (0 < ice < len(iceburg) - 1) and iceburg[ice] <= iceburg[i] < iceburg[ice - 1]:
            count += 1
        # 현 얼음이 해수면보다 높고 전 얼음이 해수면과 같거나 작으면 count+1
        if (0 < ice < len(iceburg) - 1) and iceburg[ice - 1] <= iceburg[i] < iceburg[ice]:
            count += 1
        if len(iceburg) % 2 == 0 and ice == len(iceburg)-2:
            # 현 얼음이 해수면보다 낮고 다음 얼음은 해수면보다 높을때
            if iceburg[ice] <= iceburg[i] < iceburg[ice + 1]:
                count += 1
            # 현 얼음이 해수면보다 높고 다음 얼음은 해수면보다 낮을때
            if iceburg[ice+1] <= iceburg[i] < iceburg[ice]:
                count += 1
    result.append(count)

print(max(result))