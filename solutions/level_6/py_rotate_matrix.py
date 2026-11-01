def rotate_matrix(matrix: list[list[int]]) -> list[list[int]]:
    if not matrix:
        return []

    grid: list[list[int]] = []
    rows: int = len(matrix)
    cols: int = len(matrix[0])

    for col in range(cols):
        lst: list[int] = []
        for row in range(rows - 1, -1, -1):
            lst.append(matrix[row][col])
        grid.append(lst)
    return grid


if __name__ == "__main__":
    print(rotate_matrix([[1, 2], [3, 4]]))        # [[3, 1], [4, 2]]
    print(rotate_matrix([[1, 2, 3], [4, 5, 6]]))  # [[4, 1], [5, 2], [6, 3]]
    print(rotate_matrix([[1, 2, 3]]))             # [[1], [2], [3]]
    print(rotate_matrix([[1], [2], [3]]))         # [[3, 2, 1]]
    print(rotate_matrix([[7]]))                   # [[7]]
    print(rotate_matrix([]))                      # []

"""
      1  2  3            7  4  1
      4  5  6            8  5  2
      7  8  9            9  6  3
"""
