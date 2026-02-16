# You are given an array arr[] of size n - 1 that contains distinct integers in the range from 1 to n (inclusive). This array represents a permutation of the integers from 1 to n with one element missing. 
# Your task is to identify and return the missing element.


class Solution:
    # Function ka naam 'missingNumber' se badal kar 'missingNum' kar diya hai
    def missingNum(self, arr):
        # n ki value array size + 1 hogi kyunki ek element missing hai
        n = len(arr) + 1
        
        # 1 se n tak ka mathematical sum formula: n*(n+1)/2
        expected_sum = (n * (n + 1)) // 2
        
        # Array mein maujood elements ka actual sum
        actual_sum = sum(arr)
        
        # Dono ka difference hi missing number hai
        return expected_sum - actual_sum
