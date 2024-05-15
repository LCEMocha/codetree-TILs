def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    n = int(data[0])
    first = [int(data[i + 1]) for i in range(n)]
    target = [int(data[i + n + 1]) for i in range(n)]
    visited = [False] * n
    cycle_count = 0
    max_cycle_size = 0

    # 인덱스 매핑을 위한 딕셔너리
    pos_map = {first[i]: i for i in range(n)}

    # 초기 배열의 위치를 기반으로 목표 배열의 인덱스 값 변경
    mapped_target = [pos_map[target[i]] for i in range(n)]

    for i in range(n):
        if not visited[i]:
            cycle_size = 0
            current = i
            while not visited[current]:
                visited[current] = True
                current = mapped_target[current]
                cycle_size += 1

            if cycle_size > 1:
                cycle_count += 1
                max_cycle_size = max(max_cycle_size, cycle_size)

    if cycle_count == 0:
        max_cycle_size = -1

    print(f"{cycle_count} {max_cycle_size}")

if __name__ == "__main__":
    main()