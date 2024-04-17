from collections import deque

def bfs(s):
    visited = set()
    deq = deque([(1, 0, 0)])  # screen, board, count
    visited.add((1, 0))

    while deq:
        string_screen, string_board, count = deq.popleft()

        if string_screen == s:
            return count
        
        # 1. Copy all from screen to clipboard
        if (string_screen, string_screen) not in visited and string_screen > 0:
            visited.add((string_screen, string_screen))
            deq.append((string_screen, string_screen, count + 1))
        
        # 2. Paste from clipboard to screen
        if string_board > 0 and (string_screen + string_board, string_board) not in visited:
            visited.add((string_screen + string_board, string_board))
            deq.append((string_screen + string_board, string_board, count + 1))
        
        # 3. Delete one character from screen
        if string_screen > 1 and (string_screen - 1, string_board) not in visited:  # 글자가 1개 이상일 때만 삭제
            visited.add((string_screen - 1, string_board))
            deq.append((string_screen - 1, string_board, count + 1))

s = int(input())
print(bfs(s))