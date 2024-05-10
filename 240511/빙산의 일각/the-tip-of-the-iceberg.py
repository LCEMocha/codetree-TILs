N = int(input())
heights = []
for _ in range(N):
    i = int(input())
    heights.append(i)

def max_iceberg_groups(N, heights):

    unique_heights = sorted(set(heights))
    
    # 최대 빙산 덩어리 개수 초기화
    max_groups = 0
    
    # 각 높이를 해수면 높이로 설정하고 그보다 높은 빙산들만으로 덩어리 계산
    for water_level in unique_heights:
        count = 0
        submerged = False
        for h in heights:
            if h > water_level:
                if not submerged:
                    # 새로운 덩어리 시작
                    count += 1
                    submerged = True
            else:
                # 물에 잠김
                submerged = False
        
        # 최대 덩어리 개수 업데이트
        max_groups = max(max_groups, count)
    
    return max_groups

print(max_iceberg_groups(N, heights))