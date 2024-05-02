from collections import defaultdict, deque

N, M = map(int, input().split())
def assign_items(N, M):

    # 그래프를 인접 리스트로 표현
    graph = defaultdict(list)
    for _ in range(1, M+1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    # 구역별 아이템 할당 (1부터 N까지, 인덱스는 1부터 사용하기 위해 N+1 크기로 생성)
    item_assignment = [0] * (N + 1)

    # 모든 구역에 대해 아이템 할당 시도
    for area in range(1, N + 1):
        if item_assignment[area] == 0:  # 아직 할당되지 않았다면
            available = [True] * 5  # 아이템 1, 2, 3, 4가 사용 가능한지 체크 (0 인덱스 사용 안함)

            # 현재 구역과 인접한 구역들의 사용중인 아이템 확인
            for neighbor in graph[area]:
                if item_assignment[neighbor] != 0:
                    available[item_assignment[neighbor]] = False

            # 사용 가능한 아이템 중 가장 작은 번호를 할당
            for item in range(1, 5):
                if available[item]:
                    item_assignment[area] = item
                    break

    # 출력 형식에 맞춰서 결과 반환
    return ''.join(map(str, item_assignment[1:]))

print(assign_items(N, M))