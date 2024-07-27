import time
from board import Board
from csp import recursive_backtracking, select_in_order, select_most_constrained


MAX_SOLUTIONS = 5
BOARD = "extreme"


if __name__ == "__main__":
    found_solutions = set()

    # In order
    board = Board(f"boards/{BOARD}.txt")
    solutions = []

    start_time = time.time()
    recursive_backtracking(board, solutions, select_in_order, max_solutions=MAX_SOLUTIONS)
    in_order_time = time.time() - start_time

    for solution in solutions:
        found_solutions.add(solution)


    # Most constrained
    board = Board(f"boards/{BOARD}.txt")
    solutions = []

    start_time = time.time()
    recursive_backtracking(board, solutions, select_most_constrained, max_solutions=MAX_SOLUTIONS)
    most_constrained_time = time.time() - start_time

    for solution in solutions:
        found_solutions.add(solution)


    # Conclusion
    for solution in found_solutions:
        print()
        solution.print()

    print()
    print(f"\nSolutions found: {len(found_solutions)}")
    print(f"Time taken for in_order: {round(in_order_time*1000, 2)} milliseconds")
    print(f"Time taken for most_constrained: {round(most_constrained_time*1000, 2)} milliseconds")
