# You are given a string s, and your task is to reverse the string.


class Solution:
    def reverseString(self, s: str) -> str:
        arr = list(s)      # convert to mutable list
        left = 0
        right = len(arr) - 1

        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

        return ''.join(arr)
