def evalRPN(self, tokens: List[str]) -> int:
    stack = []
    operators = {
        “+”: lambda a, b: a + b,
        “-“: lambda a, b: a – b,
        “*”: lambda a, b: a * b,
        “/”: lambda a, b: int(float(a) / b),
    }
    
    for char in tokens:
        if char in operators:
            b, a = stack.pop(), stack.pop()
            operation = operators[char]
            result = operation(a, b)
            stack.append(result)
        else:
            stack.append(int(char))
    
    return stack[0]
