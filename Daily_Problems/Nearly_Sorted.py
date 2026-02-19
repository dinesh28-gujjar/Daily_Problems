#Given an array arr[], where each element is at most k positions away from its correct position in the sorted order.
#Your task is to restore the sorted order of arr[] by rearranging the elements in place.

#Note: Don't use any sort() method.

import heapq

class Solution:
    def nearlySorted(self, arr, k):
        # Create an empty min-heap
        pq = []
        index = 0
        n = len(arr)
        
        # 1. Traverse the array
        for i in range(n):
            # Push current element into the min-heap
            heapq.heappush(pq, arr[i])
            
            # 2. If heap size exceeds k, the smallest element 
            # in the heap belongs at the current 'index'
            if len(pq) > k:
                arr[index] = heapq.heappop(pq)
                index += 1
        
        # 3. Pop the remaining elements from the heap 
        # and place them in the array
        while pq:
            arr[index] = heapq.heappop(pq)
            index += 1
        
        return arr

# Example Usage:
# sol = Solution()
# my_arr = [6, 5, 3, 2, 8, 10, 9]
# sol.nearlySorted(my_arr, 3)
# print(my_arr) # Output: [2, 3, 5, 6, 8, 9, 10]
