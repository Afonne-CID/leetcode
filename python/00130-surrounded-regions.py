def solve(board):
    # Get the dimensions of the board
    ROWS, COLS = len(board), len(board[0])

    def capture(r, c):
        # Base cases to stop DFS
        if r < 0 or c < 0 or r == ROWS or c == COLS or board[r][c] != "O":
            return

        # Mark the current 'O' as 'T' to indicate it's captured
        board[r][c] = "T"

        # Recursively capture the neighboring 'O's
        capture(r + 1, c)
        capture(r - 1, c)
        capture(r, c + 1)
        capture(r, c - 1)

    # 1. (DFS) Capture unsurrounded regions (O -> T)
    for r in range(ROWS):
        for c in range(COLS):
            if board[r][c] == "O" and (r in [0, ROWS - 1] or c in [0, COLS - 1]):
                capture(r, c)
