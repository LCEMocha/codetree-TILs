import sys
sys.setrecursionlimit(10**7)

N = int(input())
graph = []
for _ in range(N):
    l = list(input())
    graph.append(l)

def findR(i, j):
    graph[i][j] = 1
    if i+1 < len(graph[0]) and graph[i+1][j] == 'R':
        findR(i+1, j)
    if i-1 >= 0 and graph[i-1][j] == 'R':
        findR(i-1, j)
    if j-1 >= 0 and graph[i][j-1] == 'R' :
        findR(i, j-1)
    if j+1 < N and graph[i][j+1] == 'R' :
        findR(i, j+1)

def findB(i, j):
    graph[i][j] = 2
    if i+1 < len(graph[0]) and graph[i+1][j] == 'B':
        findB(i+1, j)
    if i-1 >= 0 and graph[i-1][j] == 'B':
        findB(i-1, j)
    if j-1 >= 0 and graph[i][j-1] == 'B':
        findB(i, j-1)
    if j+1 < N and graph[i][j+1] == 'B':
        findB(i, j+1)

def findG(i, j):
    graph[i][j] = 1
    if i+1 < len(graph[0]) and graph[i+1][j] == 'G':
        findG(i+1, j)
    if i-1 >= 0 and graph[i-1][j] == 'G':
        findG(i-1, j)
    if j-1 >= 0 and graph[i][j-1] == 'G':
        findG(i, j-1)
    if j+1 < N and graph[i][j+1] == 'G':
        findG(i, j+1)

count = 0
for i in range(N):
    for j in range(len(graph[0])):
        if graph[i][j] == 'R':
            findR(i,j)
            count += 1
        if graph[i][j] == 'B':
            findB(i,j)
            count += 1
        if graph[i][j] == 'G':
            findG(i,j)
            count += 1

def findRG_colorweak(i, j):
    graph[i][j] = 0
    if i+1 < len(graph[0]) and graph[i+1][j] == 1:
        findRG_colorweak(i+1, j)
    if i-1 >= 0 and graph[i-1][j] == 1:
        findRG_colorweak(i-1, j)
    if j-1 >= 0 and graph[i][j-1] == 1:
        findRG_colorweak(i, j-1)
    if j+1 < N and graph[i][j+1] == 1:
        findRG_colorweak(i, j+1)

def findB_colorweak(i, j):
    graph[i][j] = 0
    if i+1 < len(graph[0]) and graph[i + 1][j] == 2:
        findB_colorweak(i + 1, j)
    if i-1 >= 0 and graph[i - 1][j] == 2:
        findB_colorweak(i - 1, j)
    if j-1 >= 0 and graph[i][j - 1] == 2:
        findB_colorweak(i, j - 1)
    if j+1 < N and graph[i][j + 1] == 2:
        findB_colorweak(i, j + 1)


count_weak = 0
for i in range(N):
    for j in range(len(graph[0])):
        if graph[i][j] == 1:
            findRG_colorweak(i,j)
            count_weak += 1
        if graph[i][j] == 2:
            findB_colorweak(i,j)
            count_weak += 1

print(count, count_weak)