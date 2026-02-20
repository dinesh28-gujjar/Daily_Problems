# Given an integer array arr[] and an integer k, your task is to find and return the kth smallest element in the given array.
# Note: The kth smallest element is determined based on the sorted order of the array.



import random

class Solution:
    def kthSmallest(self, arr, k):
        k = k - 1  # convert to 0-index

        def partition(left, right):
            pivot_index = random.randint(left, right)
            pivot = arr[pivot_index]

            # move pivot to end
            arr[pivot_index], arr[right] = arr[right], arr[pivot_index]

            store = left
            for i in range(left, right):
                if arr[i] <= pivot:
                    arr[store], arr[i] = arr[i], arr[store]
                    store += 1

            # move pivot to final position
            arr[store], arr[right] = arr[right], arr[store]
            return store

        left, right = 0, len(arr) - 1

        while True:
            pos = partition(left, right)

            if pos == k:
                return arr[pos]
            elif pos < k:
                left = pos + 1
            else:
                right = pos - 1
