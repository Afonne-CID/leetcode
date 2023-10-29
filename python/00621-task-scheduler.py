class Solution(object):
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = collections.Counter(tasks)
        max_count = max(counter.values())
        min_time = (max_count - 1) * (n + 1) + \
                    sum(map(lambda count: count == max_count, counter.values()))
    
        return max(min_time, len(tasks))