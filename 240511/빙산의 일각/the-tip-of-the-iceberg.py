N = int(input())
heights = []
for _ in range(N):
    i = int(input())
    heights.append(i)

def max_iceberg(N, heights):
    # 빙산 높이를 담은 세트를 만들어 중복을 제거하고 정렬
    unique_heights = sorted(set(heights))
    
    # 최대 덩어리 수를 초기화
    max_groups = 0
    
    # 각 높이 -1 위치에서 물에 잠긴 빙산을 계산
    for index in range(len(unique_heights)):
        current_water_level = unique_heights[index] - 1
        count_groups = 0
        in_group = False
        
        # 전체 빙산 높이 리스트를 순회하면서 그룹 계산
        for h in heights:
            if h > current_water_level:
                if not in_group:
                    count_groups += 1
                    in_group = True
            else:
                in_group = False
        
        # 최대 그룹 수 업데이트
        max_groups = max(max_groups, count_groups)
    
    return max_groups
print(max_iceberg(N, heights))