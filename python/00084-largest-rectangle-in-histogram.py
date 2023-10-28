def largestRectangleArea(self, heights: List[int]) -> int:
    max_area = 0
    stack = []  # stack to store pairs: (index, height)

    for i, height in enumerate(heights):
        start = i
        while stack and stack[-1][1] > height:
            index, h = stack.pop()
            max_area = max(max_area, h * (i – index))
            start = index
        stack.append((start, height))

    for index, height in stack:
        max_area = max(max_area, height * (len(heights) – index))
    
    return max_area
