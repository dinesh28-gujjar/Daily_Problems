# Given a string s, reverse the string without reversing its individual words. Words are separated by dots(.).
# Note: The string may contain leading or trailing dots(.) or multiple dots(.) between two words. The returned string should only have a single dot(.) separating the words, and no extra dots should be included.


class Solution:
    def reverseWords(self, s: str) -> str:
        words = []
        n = len(s)
        i = 0
        
        while i < n:
            # skip dots
            while i < n and s[i] == '.':
                i += 1
            
            start = i
            
            # collect word
            while i < n and s[i] != '.':
                i += 1
            
            if start < i:  # valid word found
                words.append(s[start:i])
        
        # reverse words
        words.reverse()
        
        # join with single dot
        return ".".join(words)
