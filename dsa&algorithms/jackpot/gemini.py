def generate_jackpot_combinations(n=17, max_occurrence=7):
    """
    Generates and counts valid football match outcomes using backtracking.
    Prunes branches early if any outcome count exceeds max_occurrence.
    """
    outcomes = ["1", "X", "2"]
    
    # We use a list to keep track of the total valid combinations found
    stats = {"count": 0}

    def backtrack(current_combination, counts):
        # 1. Pruning: If any outcome exceeds the limit, stop this branch
        if any(c > max_occurrence for c in counts.values()):
            return

        # 2. Base Case: If we reached the required length, it's a valid combo
        if len(current_combination) == n:
            stats["count"] += 1
            # Print the first few to show it's working
            if stats["count"] <= 5:
                print(f"Match Combo {stats['count']}: {''.join(current_combination)}")
            return

        # 3. Recursive Step: Try adding '1', 'X', and '2'
        for outcome in outcomes:
            current_combination.append(outcome)
            counts[outcome] += 1
            
            backtrack(current_combination, counts)
            
            # Backtrack: undo the choice for the next iteration
            counts[outcome] -= 1
            current_combination.pop()

    # Initial state
    initial_counts = {"1": 0, "X": 0, "2": 0}
    
    print(f"Starting generation for N={n}, Max={max_occurrence}...\n")
    backtrack([], initial_counts)
    
    return stats["count"]

# Run the algorithm
if __name__ == "__main__":
    total_valid = generate_jackpot_combinations(17, 7)
    print(f"\nTotal valid combinations: {total_valid:,}")