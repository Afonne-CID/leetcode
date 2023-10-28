class Solution:
    def totalNQueens(self, n: int) -> int:
        result = 0

        cols = set()
        posdiag = set()
        negdiag = set()

        def backtrack(row):
            nonlocal result  # To modify the outer result variable

            # Base case: If we have successfully placed queens in all rows, increment the result.
            if row == n:
                result += 1
                return

            for col in range(n):
                # Check if the current position is not attacked by previously placed queens
                if col in cols or (row + col) in posdiag or (row - col) in negdiag:
                    continue

                # Mark the current position as occupied by a queen
                cols.add(col)
                posdiag.add(row + col)
                negdiag.add(row - col)

                # Move to the next row
                backtrack(row + 1)

                # Backtrack by removing the queen from the current position
                cols.remove(col)
                posdiag.remove(row + col)
                negdiag.remove(row - col)

        backtrack(0)  # Start the backtracking from the first row
        return result
