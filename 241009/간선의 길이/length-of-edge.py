import heapq

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]  # 인덱스가 1부터 시작하므로
input_vals = []

for _ in range(M):
    u, v, w = map(int, input().split())  # u: 정점 1, v: 정점 2, w: 가중치
    input_vals.append([u, v, w])
    graph[u].append((v, w))  # u에서 v로 가는 간선 (가중치 w)
    graph[v].append((u, w))  # 만약 무방향 그래프라면, v에서 u로 가는 간선도 추가

def dijkstra(N, graph, start):
    distances = [float('inf')] * (N + 1)
    distances[start] = 0

    pq = [(0, start)]

    while pq :
        current_dist, current_node = heapq.heappop(pq)
        
        # 이미 처리된 노드라면 스킵
        if current_dist > distances[current_node]:
            continue
        
        # 인접 노드 확인
        for neighbor, weight in graph[current_node]:
            distance = current_dist + weight
            
            # 더 짧은 경로를 발견하면 업데이트
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return distances

previous_shortcut = dijkstra(N, graph, 1)[-1]
doubled_max_shortcut = 0

for i in range(M):
    input_vals[i][-1] = input_vals[i][-1]*2
    new_graph = [[] for _ in range(N + 1)]
    for u, v, w in input_vals:
        new_graph[u].append((v, w))  
        new_graph[v].append((u, w))        
    doubled_max_shortcut = max(doubled_max_shortcut, dijkstra(N, new_graph, 1)[-1])
    input_vals[i][-1] = input_vals[i][-1]//2

print(doubled_max_shortcut - previous_shortcut)