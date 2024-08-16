sequence = int(input())

def seq(s):
    if s == 0:
        return 0
    if s == 1:
        return 1
    if s == 2:
        return 1
    else:
        return seq(s-1) + seq(s-2)


print(seq(sequence))