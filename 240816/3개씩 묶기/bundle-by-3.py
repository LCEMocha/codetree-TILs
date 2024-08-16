from collections import deque

number = int(input())
numbers = list(map(int, input().split()))
remove_sum = 0

numbers.sort(reverse=True)
numbers_deque = deque(numbers)
while len(numbers_deque) >= 3:
    temp = numbers_deque.popleft()
    temp2 = numbers_deque.popleft()
    remove_sum += (temp + temp2)
    numbers_deque.popleft()

while len(numbers_deque) > 0:
    temp = numbers_deque.popleft()
    remove_sum += temp

print(remove_sum)