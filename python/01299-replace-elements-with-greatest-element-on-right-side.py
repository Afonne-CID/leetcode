def replaceElements(arr):
    right_max = -1  # Initialize the right maximum as -1
    for i in range(len(arr) - 1, -1, -1):
        new_max = max(right_max, arr[i])
        arr[i] = right_max
        right_max = new_max
    return arr
