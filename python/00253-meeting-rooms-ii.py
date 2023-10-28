def minMeetingRooms(intervals):
    start_times = []
    end_times = []

    # Populate start and end time arrays
    for start, end in intervals:
        start_times.append((start, 1))
        end_times.append((end, -1))

    # Sort the combined array based on time and event type
    time = start_times + end_times
    time.sort(key=lambda x: (x[0], x[1]))

    count = 0
    max_count = 0

    for t in time:
        count += t[1]
        max_count = max(max_count, count)

    return max_count
