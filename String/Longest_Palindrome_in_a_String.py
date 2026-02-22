# Given a string s, your task is to find the longest palindromic substring within s.
# A substring is a contiguous sequence of characters within a string, defined as s[i...j] where 0 ≤ i ≤ j < len(s).
# A palindrome is a string that reads the same forward and backward. More formally, s is a palindrome if reverse(s) == s.
# Note: If there are multiple palindromic substrings with the same length, return the first occurrence of the longest palindromic substring from left to right.


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ""

        start = 0
        max_len = 1

        def expand(l, r):
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            return l + 1, r - 1   # valid palindrome boundaries

        for i in range(n):

            # Odd length palindrome
            l1, r1 = expand(i, i)
            if (r1 - l1 + 1) > max_len:
                start = l1
                max_len = r1 - l1 + 1

            # Even length palindrome
            l2, r2 = expand(i, i + 1)
            if (r2 - l2 + 1) > max_len:
                start = l2
                max_len = r2 - l2 + 1

        return s[start:start + max_len]
