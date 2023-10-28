import collections
from collections import deque
from typing import List

def ladderLength(beginWord: str, endWord: str, wordList: List[str]) -> int:
    if endWord not in wordList:
        return 0

    # Build the adjacency list
    neighbors = collections.defaultdict(list)
    wordList.append(beginWord)
    for word in wordList:
        for j in range(len(word)):
            pattern = word[:j] + "*" + word[j + 1 :]
            neighbors[pattern].append(word)

    # Initialize data structures for BFS
    visited = set([beginWord])
    queue = deque([beginWord])
    path_length = 1

    while queue:
        for i in range(len(queue)):
            word = queue.popleft()
            if word == endWord:
                return path_length
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1 :]
                for neighbor in neighbors[pattern]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
        path_length += 1

    return 0
