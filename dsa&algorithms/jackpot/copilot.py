from typing import Generator, List

def generate_combinations(N: int = 17, max_occurrence: int = 7) -> Generator[str, None, None]:
    """
    Generate all valid football match outcome combinations of length N
    using { '1', 'X', '2' } with constraints:
    - Count of '1' <= max_occurrence
    - Count of 'X' <= max_occurrence
    - Count of '2' <= max_occurrence
    
    Memory-efficient: uses recursion + generator (no full storage).
    """

    outcomes = ["1", "X", "2"]

    def backtrack(prefix: List[str], count_1: int, count_X: int, count_2: int):
        # Stop if prefix length reaches N
        if len(prefix) == N:
            yield "".join(prefix)
            return

        # Try each possible outcome
        for outcome in outcomes:
            if outcome == "1" and count_1 < max_occurrence:
                yield from backtrack(prefix + ["1"], count_1 + 1, count_X, count_2)
            elif outcome == "X" and count_X < max_occurrence:
                yield from backtrack(prefix + ["X"], count_1, count_X + 1, count_2)
            elif outcome == "2" and count_2 < max_occurrence:
                yield from backtrack(prefix + ["2"], count_1, count_X, count_2 + 1)

    return backtrack([], 0, 0, 0)


# Example usage: print first 10 valid combinations
if __name__ == "__main__":
    gen = generate_combinations(N=17, max_occurrence=7)
    for i, combo in enumerate(gen):
        if i < 100:
            print(combo)
        else:
            break