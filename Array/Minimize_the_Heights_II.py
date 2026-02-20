# Given an array arr[] denoting heights of n towers and a positive integer k.For each tower, you must perform exactly one of the following operations exactly once.
# Increase the height of the tower by k. Decrease the height of the tower by k. Find out the minimum possible difference between the height of the shortest and tallest towers after you have modified each tower.
# Note: It is compulsory to increase or decrease the height by k for each tower. After the operation, the resultant array should not contain any negative integers.



class Solution:
    def getMinDiff(self, arr, k):

        n = len(arr)
        if n == 1:
            return 0

        arr.sort()

        # initial difference
        ans = arr[n - 1] - arr[0]

        smallest = arr[0] + k
        largest = arr[n - 1] - k

        for i in range(n - 1):

            if arr[i + 1] - k < 0:
                continue

            high = max(arr[i] + k, largest)
            low = min(smallest, arr[i + 1] - k)

            ans = min(ans, high - low)

        return ans
