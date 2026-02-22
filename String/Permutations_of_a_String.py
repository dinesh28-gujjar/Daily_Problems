# Given a string s, which may contain duplicate characters, your task is to generate and return an array of all unique permutations of the string. 
# You can return your answer in any order.


class Solution:
    def findPermutation(self, s):
        result = []
        freq = {}

        # Frequency count
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        # Backtracking
        def backtrack(path):
            if len(path) == len(s):
                result.append("".join(path))
                return

            for ch in sorted(freq.keys()):
                if freq[ch] > 0:
                    path.append(ch)
                    freq[ch] -= 1

                    backtrack(path)

                    path.pop()
                    freq[ch] += 1

        backtrack([])
        return result
