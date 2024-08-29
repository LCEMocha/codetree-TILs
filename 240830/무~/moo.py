N = int(input())

def get_len(t) :
    if t == 0 :
        return 3
    return 2 * get_len(t - 1) + (t + 3)

def get_N(N, t):
    if t == 0:
        return "moo"[N - 1]
    
    prev_len = get_len(t-1)
    middle_length = t+3

    if N <= prev_len:
        return get_N(N, t-1)
    if N > prev_len:
        return get_N(N-middle_length-prev_len, t-1)
    if N == prev_len:
        if N == middle_length+1:
            return 'm'
        else:
            return 'o'
    
t = 0
while get_len(t) < N:
    t += 1

print(get_N(N, t))