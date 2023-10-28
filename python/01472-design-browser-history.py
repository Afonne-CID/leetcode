class BrowserHistory:    
    def __init__(self, homepage: str):
        self.i = 0
        self.length = 1
        self.history = [homepage]

    # Visit a URL
    # Time complexity: O(1)
    def visit(self, url: str) -> None:
        if len(self.history) < self.i + 2:
            self.history.append(url)
        else:
            self.history[self.i + 1] = url
        self.i += 1
        self.length = self.i + 1

    # Move back in history
    # Time complexity: O(1)
    def back(self, steps: int) -> str:
        self.i = max(self.i - steps, 0)
        return self.history[self.i]

    # Move forward in history
    # Time complexity: O(1)
    def forward(self, steps: int) -> str:
        self.i = min(self.i + steps, self.length - 1)
        return self.history[self.i]
