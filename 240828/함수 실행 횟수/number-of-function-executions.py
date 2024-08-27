n = int(input())

def count(N) :
    if (N < 2) :
        return 1
    else :
        if N == 2 :
            return 3
        if N == 3 :
            return 5
        else:
            return count(N-1) + count(N-2) + 1

print(count(n)%1000000007)