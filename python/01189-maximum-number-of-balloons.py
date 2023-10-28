from collections import Counter

def maxNumberOfBalloons(text: str) -> int:
    # Initialize character counts for 'balloon'
    balloon = Counter("balloon")

    # Initialize character counts for the text
    countText = Counter(text)

    # Initialize the result to the maximum number of instances
    result = len(text)

    # Iterate through characters in 'balloon' and calculate the minimum instances
    for char in balloon:
        result = min(result, countText[char] // balloon[char])

    return result
