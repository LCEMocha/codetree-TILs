def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    heights = list(map(int, data[1:n+1]))
    
    # 빙산 높이 중복 제거 및 정렬
    unique_heights = sorted(set(heights), reverse=True)
    height_to_index = {height: idx for idx, height in enumerate(unique_heights)}
    
    # 높이별 인덱스 위치 저장
    index_arr = [[] for _ in range(len(unique_heights))]
    for idx, height in enumerate(heights, 1):
        index_arr[height_to_index[height]].append(idx)
    
    visited = [False] * (n + 2)
    result = 0
    answer = 0
    
    # 빙산 높이가 높은 순으로 순회
    for i in range(len(unique_heights)):
        for cur_idx in index_arr[i]:
            if not visited[cur_idx - 1] and not visited[cur_idx + 1]:
                result += 1
            elif visited[cur_idx - 1] and visited[cur_idx + 1]:
                result -= 1
            
            # 현재 인덱스 방문 처리
            visited[cur_idx] = True
        
        # 최대 그룹 수 갱신
        answer = max(answer, result)
    
    print(answer)

if __name__ == "__main__":
    main()