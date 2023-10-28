def isValidSudoku(self, board: List[List[str]]) -> bool:
    # Initialize hash sets for rows, columns, and sub-grids
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    subgrids = {(i // 3, j // 3): set() for i in range(9) for j in range(9)}

    for i in range(9):
        for j in range(9):
            cell = board[i][j]

            if cell == ‘.’:
                continue

            # Check row
            if cell in rows[i]:
                return False
            rows[i].add(cell)

            # Check column
            if cell in cols[j]:
                return False
            cols[j].add(cell)

            # Check sub-grid
            subgrid = subgrids[(i // 3, j // 3)]
            if cell in subgrid:
                return False
            subgrid.add(cell)

    return True
