sequence1, sequence2 = 0, 1
print(sequence1)
print(sequence2)
for _ in range(18):
    sequence_next = sequence1 + sequence2
    print(sequence_next)
    sequence1, sequence2 = sequence2, sequence_next