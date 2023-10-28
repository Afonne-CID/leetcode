def isSubsequence(s: str, t: str) -> bool:
    start = 0
    for char in s:
        start = t.find(char, start)
        if start == -1:
            return False
        start += 1
    return True
