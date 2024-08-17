import copy

N = int(input())
sequence = list(map(int, input().split()))
third = list(map(int, input().split()))
reverse_seq = [0] * (N+1)

def reverse_sequence(seq, reverse_seq):
    for i in range(len(seq)):
        reverse_seq[seq[i]] = i
    reverse_seq = reverse_seq[1:]
    #reverse_seq = [i+1 for i in reverse_seq]
    return reverse_seq

def original_order(third, seq, reverse_seq):
    reverse_seq = reverse_sequence(seq, reverse_seq)
    for q in range(3):
        third_copy = copy.deepcopy(third)
        for i in range(len(third)) :
            third[reverse_seq[i]] = third_copy[i]
    return third

third = original_order(third, sequence, reverse_seq)
for i in third:
    print(i)