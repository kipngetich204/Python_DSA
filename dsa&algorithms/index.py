import random
import time
import math
import copy
import tracemalloc

# ==========================================================
#  SUDOKU UTILITIES
# ==========================================================

def generate_puzzle(rows: int = 9, cols: int = 9):
    """
    Generate a random Sudoku-like puzzle (not guaranteed valid).
    Each cell is filled with a random number from 1-9.
    """
    print("[DEBUG] Generating puzzle...")
    matrix = []
    for i in range(rows):
        row = [random.randint(1, 9) for _ in range(cols)]
        matrix.append(row)
        print(f"[TRACE] Row {i}: {row}")
    return matrix


def display(board):
    """
    Pretty-print the Sudoku board, replacing 0 with '_'.
    """
    print("[DEBUG] Displaying board:")
    for row in board:
        line = " ".join(str(val) if val != 0 else "_" for val in row)
        print("[TRACE]", line)


def is_valid_sudoku(board):
    """
    Validate Sudoku rules:
    - Rows contain no duplicates (ignoring 0).
    - Columns contain no duplicates.
    - 3x3 sub-boxes contain no duplicates.
    """
    print("[DEBUG] Validating Sudoku...")

    def is_unit_valid(unit, unit_type, index):
        unit_no_zeros = [num for num in unit if num != 0]
        valid = len(unit_no_zeros) == len(set(unit_no_zeros))
        print(f"[TRACE] {unit_type} {index}: {unit} -> {'Valid' if valid else 'Invalid'}")
        return valid

    for i, row in enumerate(board):
        if not is_unit_valid(row, "Row", i):
            return False

    for col in range(9):
        if not is_unit_valid([board[row][col] for row in range(9)], "Col", col):
            return False

    for box_row in range(0, 9, 3):
        for box_col in range(0, 9, 3):
            box = [board[box_row + i][box_col + j] for i in range(3) for j in range(3)]
            if not is_unit_valid(box, f"Box ({box_row},{box_col})", ""):
                return False

    return True


def repeat():
    """
    Keep generating Sudoku boards until a valid one is found.
    Trace each attempt with debug info.
    """
    count = 0
    while True:
        print(f"[DEBUG] Attempt {count+1}")
        puzzle = generate_puzzle()
        valid = is_valid_sudoku(puzzle)
        display(puzzle)
        count += 1
        if valid:
            print(f"✅ Valid puzzle found after {count} attempts")
            break
        else:
            print(f"❌ Invalid puzzle (attempt {count})\n")
            time.sleep(1)


# ==========================================================
#  SEARCHING ALGORITHMS
# ==========================================================

def binary_search(array, target):
    """Iterative binary search with trace."""
    print(f"[DEBUG] Starting binary search for {target} in {array}")
    low, high = 0, len(array) - 1
    while low <= high:
        mid = math.floor(low + (high - low) / 2)
        print(f"[TRACE] low={low}, high={high}, mid={mid}, value={array[mid]}")
        if array[mid] == target:
            print(f"✅ Found {target} at index {mid}")
            return mid
        elif array[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    print("❌ Target not found")
    return -1


def recursion_binary_search(arr, low, high, target):
    """Recursive binary search with trace."""
    print(f"[TRACE] Recursion: low={low}, high={high}")
    if low <= high:
        mid = math.floor(low + (high - low) / 2)
        print(f"[TRACE] Checking index {mid}, value={arr[mid]}")
        if arr[mid] == target:
            print(f"✅ Found {target} at index {mid}")
            return mid
        elif arr[mid] < target:
            return recursion_binary_search(arr, mid + 1, high, target)
        else:
            return recursion_binary_search(arr, low, mid - 1, target)
    print("❌ Target not found")
    return -1


def traced_binary_search(arr, low, high, target, depth=0):
    """
    Binary search with detailed trace of recursion steps.
    """
    indent = "  " * depth
    print(f"{indent}[TRACE] Searching: low={low}, high={high}")

    if low <= high:
        mid = (low + high) // 2
        print(f"{indent}[TRACE] Checking middle index {mid} (value: {arr[mid]})")

        if arr[mid] == target:
            print(f"{indent}✅ Found target at index {mid}")
            return mid
        elif arr[mid] < target:
            print(f"{indent}→ Going right")
            return traced_binary_search(arr, mid + 1, high, target, depth + 1)
        else:
            print(f"{indent}← Going left")
            return traced_binary_search(arr, low, mid - 1, target, depth + 1)

    print(f"{indent}❌ Target not found")
    return -1


# ==========================================================
#  LINKED LIST IMPLEMENTATION
# ==========================================================
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        print(f"[DEBUG] Appending {data}")
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        print("[DEBUG] Displaying Linked List:")
        current = self.head
        while current:
            print(f"[TRACE] Node: {current.data}")
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# ==========================================================
#  ARRAY ROTATION + BENCHMARKING
# ==========================================================

def rotate(arr, r):
    """Rotate using slicing manually with trace."""
    print(f"[DEBUG] Rotating array by {r} using slicing")
    result = arr[r:] + arr[:r]
    print(f"[TRACE] Result head: {result[:10]}...")
    return result


def rota(arr, k):
    """Rotate array using reversal algorithm with trace."""
    k %= len(arr)
    print(f"[DEBUG] Rotating array by {k} using reversal")

    def reverse(start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

    reverse(0, len(arr) - 1)
    reverse(0, len(arr) - k - 1)
    reverse(len(arr) - k, len(arr) - 1)
    print(f"[TRACE] Result head: {arr[:10]}...")
    return arr


def benchmark(name, func, arr, r):
    arr_copy = copy.deepcopy(arr)

    print(f"[DEBUG] Benchmarking {name}")
    tracemalloc.start()
    start_time = time.perf_counter()

    func(arr_copy, r)

    end_time = time.perf_counter()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    elapsed_time = end_time - start_time
    print(f"{name.ljust(10)} | Time: {elapsed_time:.5f}s | Peak Memory: {peak / (1024 ** 2):.2f} MB")


# ==========================================================
#  MAIN DEMO
# ==========================================================
if __name__ == "__main__":
    # Binary search demo
    arr = [1, 3, 5, 7, 9, 11]
    print("\nBinary Search Trace:")
    traced_binary_search(arr, 0, len(arr) - 1, 7)

    # Linked List demo
    print("\nLinked List:")
    ll = LinkedList()
    for val in [10, 20, 30]:
        ll.append(val)
    ll.display()

    # Benchmark rotation
    print("\nBenchmarking rotation functions:")
    n = 100_000
    r = 12_345
    big_array = list(range(n))
    benchmark("rotate", rotate, big_array, r)
    benchmark("rota", rota, big_array, r)
