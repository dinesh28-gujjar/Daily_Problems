# Given two non-empty strings s1 and s2, consisting only of lowercase English letters, determine whether they are anagrams of each other or not.
# Two strings are considered anagrams if they contain the same characters with exactly the same frequencies, regardless of their order.



class Solution:
    def areAnagrams(self, s1: str, s2: str) -> bool:

        # Step 1: Length check
        if len(s1) != len(s2):
            return False

        # Step 2: Frequency array
        freq = [0] * 26

        # Step 3: Count characters
        for i in range(len(s1)):
            freq[ord(s1[i]) - ord('a')] += 1
            freq[ord(s2[i]) - ord('a')] -= 1

        # Step 4: Verify all zero
        for val in freq:
            if val != 0:
                return False

        return True
