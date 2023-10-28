def merge(self, intervals: List[List[int]]) -> List[List[int]:
    # Sort intervals by their start values
    intervals.sort(key=lambda pair: pair[0])
    output = [intervals[0]]  # Initialize the output with the first interval

    for start, end in intervals[1:]:
        lastEnd = output[-1][1]  # Get the end value of the last interval in the output

        if start <= lastEnd:
            # Merge the intervals
            output[-1][1] = max(lastEnd, end)
        else:
            output.append([start, end])  # Add the non-overlapping interval to the output

    return output
