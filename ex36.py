def distance(strand_a, strand_b):
    total = 0
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    for a, b in zip(strand_a.upper(), strand_b.upper()):
        if a != b:
            total += 1
    return total
