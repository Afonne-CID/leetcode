def findRepeatedDnaSequences(s: str) -> list[str]:
    result = set()
    seen = set()
    for i in range(len(s) - 9):
        current = s[i:i+10]
        if current in seen:
            result.add(current)
        seen.add(current)
    return list(result)
