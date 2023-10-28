class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        result = 0
        current_sum = sum(arr[:k - 1])

        for left in range(len(arr) - k + 1):
            current_sum += arr[left + k - 1]
            if (current_sum / k) >= threshold:
                result += 1
            current_sum -= arr[left]

        return result
