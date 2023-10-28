def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    answer = collections.defaultdict(list)

    for string in strs:
        count = [0] * 26
        for character in string:
            count[ord(character) – ord(“a”)] += 1
        answer[tuple(count)].append(string)
    return answer.values()
