
class Board(list):
    Possibe_values = [str(i+1) for i in range(9)]

    def __init__(self, board_file: str) -> None:
        """
        This is a list of strings, where each string represents a row.

        Empty spaces are represented by a space: ''.
        """
        if board_file:
            self.init_from_file(board_file)

    def init_from_file(self, board_file: str):
        with open(board_file) as file:
            rows = [row.strip().replace("x", " ") for row in file.readlines()]

            if len(rows) != 9:
                raise Exception("Make sure the board has 9 rows!")

            for i, row in enumerate(rows):
                if len(row) != 9:
                    print(f"Error on row {i}:")
                    raise Exception("Make sure the board has 9 columns everywhere!")

                for value in row:
                    try:
                        _ = None if value == " " else int(value)
                    except ValueError:
                        raise Exception("Only have spaces and numbers on the board!")

                self.append(row)

    @property
    def has_unassigned_spaces(self) -> bool:
        for row in self:
            for value in row:
                if value == " ":
                    return True
        return False

    def clone(self) -> list:
        clone = Board(None)
        for row in self:
            clone.append(row)
        return clone

    def add_value(self, i: int, j: int, new_value: int):
        self[i] = f"{self[i][:j]}{new_value}{self[i][j+1:]}"

    def remove_value(self, i: int, j: int):
        self[i] = f"{self[i][:j]} {self[i][j+1:]}"

    def is_value_constraint_consistent(self, i: int, j: int, value: str):
        for row in self:
            if row[j] == value:
                return False

        for space in self[i]:
            if space == value:
                return False

        for row_offset in self.get_offset_for_group(i):
            for col_offset in self.get_offset_for_group(j):
                if self[i+row_offset][j+col_offset] == value:
                    return False

        return True

    def get_offset_for_group(self, row_col: int) -> tuple:
        if row_col in (0, 3, 6):
            return (1, 2)
        elif row_col in (1, 4, 7):
            return (-1, 1)
        elif row_col in (2, 5, 8):
            return (-2, -1)

    def get_row_constraints(self) -> list:
        return [sum([0 if space == " " else 1 for space in row]) for row in self]

    def get_col_constraints(self) -> list:
        return [sum(0 if self[i][j] == " " else 1 for i in range(9)) for j in range(9)]

    def get_block_constraints(self, i: int, j: int) -> list:
        count = 0
        for row_offset in self.get_offset_for_group(i):
            for col_offset in self.get_offset_for_group(j):
                if self[i+row_offset][j+col_offset] != " ":
                    count += 1
        return count

    def print(self) -> None:
        print(",-----,-----,-----,")
        for i, row in enumerate(self):
            if i in (3, 6):
                print("|-----|-----|-----|")
            print(f"|{row[0]} {row[1]} {row[2]}|{row[3]} {row[4]} {row[5]}|{row[6]} {row[7]} {row[8]}|")
        print("'-----'-----'-----'")

    def __hash__(self):
        return hash(tuple(self))

    def __eq__(self, other):
        if isinstance(other, Board):
            return super().__eq__(other)
        return False
