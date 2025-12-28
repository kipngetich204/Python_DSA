def generate_combinations(N=17, max_occurrence=7):
    """
    Generates valid combinations and returns total count.
    """

    outcomes = ["1", "X", "2"]
    total_count = 0

    def backtrack(pos, current, counts):
        nonlocal total_count

        # Early pruning
        if any(counts[o] > max_occurrence for o in outcomes):
            return

        if pos == N:
            total_count += 1
            yield "".join(current)
            return

        for o in outcomes:
            current.append(o)
            counts[o] += 1

            yield from backtrack(pos + 1, current, counts)

            current.pop()
            counts[o] -= 1

    generator = backtrack(
        pos=0,
        current=[],
        counts={"1": 0, "X": 0, "2": 0}
    )

    return generator, lambda: total_count

gen, count_fn = generate_combinations(N=17, max_occurrence=7)

for _ in range(5):
    print(next(gen))

# Exhaust generator to compute total count
for _ in gen:
    pass

print("Total valid combinations:", count_fn())