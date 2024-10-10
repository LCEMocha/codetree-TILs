import heapq

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]  # 인덱스가 1부터 시작하므로
edges = []

for _ in range(M):
    u, v, w = map(int, input().split())  # u: 정점 1, v: 정점 2, w: 가중치
    edges.append((u, v, w))
    graph[u].append((v, w))  # u에서 v로 가는 간선 (가중치 w)
    graph[v].append((u, w))  # 무방향 그래프니 v에서 u로 가는 간선도 추가

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

# 1. 원래 최단 거리 계산
original_dist = dijkstra(N, graph, 1)
previous_shortcut = original_dist[N]  # 1번 정점에서 N번 정점까지의 최단 거리

doubled_max_shortcut = 0

# 2. 각 간선을 2배로 늘리고 최단 거리 계산
for u, v, w in edges:
    for i, (neighbor, weight) in enumerate(graph[u]):
        if neighbor == v and weight == w:
            graph[u][i] = (v, 2 * w)
        
        if neighbor == u and weight == w:
            graph[v][i] = (u, 2*w)
    
    new_dist = dijkstra(N, graph, 1)
    new_shortcut = new_dist[N]

    if new_shortcut != float('inf'):
        doubled_max_shortcut = max(doubled_max_shortcut, new_shortcut)
    
    # 간선 (u, v)의 가중치를 원래대로 복구
    for idx, (neighbor, weight) in enumerate(graph[u]):
        if neighbor == v and weight == 2 * w:
            graph[u][idx] = (v, w)  # 원래 값으로 복구
    
    for idx, (neighbor, weight) in enumerate(graph[v]):
        if neighbor == u and weight == 2 * w:
            graph[v][idx] = (u, w)  # 원래 값으로 복구

# 3. 결과 출력
print(doubled_max_shortcut - previous_shortcut)