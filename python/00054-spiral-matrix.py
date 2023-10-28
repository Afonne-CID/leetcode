def spiralOrder(matrix):
    if not matrix:
        return []

    result = []
    left, right = 0, len(matrix[0]) - 1
    top, bottom = 0, len(matrix) - 1

    while left <= right and top <= bottom:
        # Traverse the top row
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1

        # Traverse the right column
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1

        if not (left <= right and top <= bottom):
            break

        # Traverse the bottom row
        for i in range(right, left - 1, -1):
            result.append(matrix[bottom][i])
        bottom -= 1

        # Traverse the left column
        for i in range(bottom, top - 1, -1):
            result.append(matrix[i][left])
        left += 1

    return result
