class Solution:
    def __find(self, n: int) -> int:
        while n != self.parents.get(n, n):
            n = self.parents.get(n, n)
        return n

    def __connect(self, n: int, m: int) -> None:
        pn = self.__find(n)
        pm = self.__find(m)
        if pn == pm:
            return
        if self.heights.get(pn, 1) > self.heights.get(pm, 1):
            self.parents[pn] = pm
        else:
            self.parents[pm] = pn
            self.heights[pm] = self.heights.get(pn, 1) + 1
        self.components -= 1

    def valid_tree(self, n: int, edges: List[List[int]) -> bool:
        self.parents = {}
        self.heights = {}
        self.components = n

        for e1, e2 in edges:
            if self.__find(e1) == self.__find(e2):  # 'redundant' edge
                return False
            self.__connect(e1, e2)

        return self.components == 1  # The forest contains one tree
