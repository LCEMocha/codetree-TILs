import sys
input = sys.stdin.readline

n, k = map(int, input().split())
a1, a2 = map(int, input().split())
b1, b2 = map(int, input().split())

l = [i+1 for i in range(n)]

for _ in range(k):
    l[a1-1 : a2] = l[a1-1 : a2][::-1]
    l[b1-1 : b2] = l[b1-1 : b2][::-1]

for i in l:
    print(i)