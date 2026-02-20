# Given an array of integers arr[] representing non-negative integers, arrange them so that after concatenating all of them in order, it results in the largest possible number. 
# Since the result may be very large, return it as a string.



from functools import cmp_to_key

class Solution:
    def findLargest(self, arr):

        # convert numbers to strings
        arr = list(map(str, arr))

        # custom comparator
        def compare(a, b):
            if a + b > b + a:
                return -1
            elif a + b < b + a:
                return 1
            else:
                return 0

        # sort based on concatenation rule
        arr.sort(key=cmp_to_key(compare))

        # handle all zeros case
        if arr[0] == "0":
            return "0"

        return "".join(arr)
