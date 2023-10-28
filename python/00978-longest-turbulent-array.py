def maxTurbulenceSize(arr):
    left, right = 0, 1  # Initialize left and right pointers for the sliding window.
    result, prev = 1, ""  # Initialize the result and previous sign.

    while right < len(arr):
        if arr[right - 1] > arr[right] and prev != ">":
            result = max(result, right - left + 1)
            right += 1
            prev = ">"
        elif arr[right - 1] < arr[right] and prev != "<":
            result = max(result, right - left + 1)
            right += 1
            prev = "<"
        else:
            right = right + 1 if arr[right] == arr[right - 1] else right
            left = right - 1
            prev = ""

    return result
