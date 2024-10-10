import heapq
import sys

INF = sys.maxsize

def dijkstra(n, graph, start):
    dist = [INF] * (n + 1)
    dist[start] = 0
    pq = []
    heapq.heappush(pq, (0, start))
    
    while pq:
        current_dist, u = heapq.heappop(pq)
        
        if current_dist > dist[u]:
            continue
        
        for v, weight in graph[u]:
            if dist[v] > dist[u] + weight:
                dist[v] = dist[u] + weight
                heapq.heappush(pq, (dist[v], v))
    
    return dist

def find_max_increase(n, m, edges):
    # 그래프 초기화
    graph = [[] for _ in range(n + 1)]
    
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    # 1. 원래의 최단 거리 계산
    original_dist = dijkstra(n, graph, 1)
    original_shortest = original_dist[n]
    
    # 2. 각 간선을 2배로 했을 때의 최단 거리 변화를 계산
    max_increase = 0
    for u, v, w in edges:
        # 간선 (u, v)의 길이를 2배로 늘림
        graph[u].remove((v, w))
        graph[v].remove((u, w))
        graph[u].append((v, 2 * w))
        graph[v].append((u, 2 * w))
        
        # 최단 거리 계산
        new_dist = dijkstra(n, graph, 1)
        new_shortest = new_dist[n]
        
        # 변화량 계산
        if new_shortest != INF:  # 만약 갈 수 있는 경로가 존재할 때
            max_increase = max(max_increase, new_shortest - original_shortest)
        
        # 간선 복구
        graph[u].remove((v, 2 * w))
        graph[v].remove((u, 2 * w))
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    return max_increase

# 입력 처리
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# 결과 출력
result = find_max_increase(n, m, edges)
print(result)