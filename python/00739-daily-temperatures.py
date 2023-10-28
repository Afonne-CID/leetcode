def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    n = len(temperatures)
    answer = [0] * n
    stack = []  # A stack to keep track of temperatures and their indices

    for i in range(n):
        while stack and temperatures[i] > stack[-1][0]:
            temp, index = stack.pop()
            answer[index] = i – index
        stack.append((temperatures[i], i))

    return answer
