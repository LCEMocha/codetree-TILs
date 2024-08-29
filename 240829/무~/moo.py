def find_nth_character(N):
    def length_of_S(t):
        if t == 0:
            return 3  # S(0)의 길이 ("moo")
        return 2 * length_of_S(t - 1) + (t + 3)

    def solve(N, t):
        if t == 0:
            return "moo"[N - 1]
        
        prev_len = length_of_S(t - 1)
        middle_len = t + 3
        
        if N <= prev_len:
            return solve(N, t - 1)
        elif N > prev_len + middle_len:
            return solve(N - prev_len - middle_len, t - 1)
        else:
            if N == prev_len + 1:
                return 'm'
            else:
                return 'o'
    
    t = 0
    while length_of_S(t) < N:
        t += 1
    
    return solve(N, t)

N = int(input())
print(find_nth_character(N))