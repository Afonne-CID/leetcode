def canAttendMeetings(intervals):
    # Sort the intervals based on their start times
    intervals.sort(key=lambda i: i[0])

    for i in range(1, len(intervals)):
        i1 = intervals[i - 1]
        i2 = intervals[i]

        # Check if the end time of the previous interval is greater than the start time of the current interval
        if i1[1] > i2[0]:
            return False

    # If no overlaps were found, return True
    return True
