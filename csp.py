from board import Board


def recursive_backtracking(board: Board, solutions: list, select_func, max_solutions: int = 1):
    if not board.has_unassigned_spaces:
        solutions.append(board.clone())
        return

    i, j = select_func(board)
    for value in board.Possibe_values:
        if board.is_value_constraint_consistent(i, j, value):
            board.add_value(i, j, value)

            recursive_backtracking(board, solutions, select_func, max_solutions=max_solutions)
            if len(solutions) >= max_solutions:
                return

            board.remove_value(i, j)


def select_in_order(board: Board) -> tuple:
    for i, row in enumerate(board):
        for j, col in enumerate(row):
            if col == " ":
                return i, j
    return 0, 0


def select_most_constrained(board: Board) -> tuple:
    most_constrained = (0, 0, 0)

    for i, row in enumerate(board):
        for j, col in enumerate(row):
            if col == " ":

                constraints_number = board.get_number_of_constraints(i, j)
                if constraints_number > most_constrained[2]:
                    most_constrained = (i, j, constraints_number)

    return most_constrained[0], most_constrained[1]
