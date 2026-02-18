# Given an array of integers arr[]. You have to find the Inversion Count of the array. 
# Note : Inversion count is the number of pairs of elements (i, j) such that i < j and arr[i] > arr[j].


class Solution:
    def inversionCount(self, arr):
        n = len(arr)
        temp_arr = [0] * n
        return self._merge_sort(arr, temp_arr, 0, n - 1)

    def _merge_sort(self, arr, temp_arr, left, right):
        inv_count = 0
        if left < right:
            mid = (left + right) // 2
            
            # Left half ke inversions
            inv_count += self._merge_sort(arr, temp_arr, left, mid)
            # Right half ke inversions
            inv_count += self._merge_sort(arr, temp_arr, mid + 1, right)
            # Merging ke waqt ke inversions
            inv_count += self._merge(arr, temp_arr, left, mid, right)
            
        return inv_count

    def _merge(self, arr, temp_arr, left, mid, right):
        i = left    # Left subarray ka starting index
        j = mid + 1 # Right subarray ka starting index
        k = left    # Temp array ka index
        inv_count = 0
        
        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                temp_arr[k] = arr[i]
                i += 1
            else:
                # Inversion mil gaya!
                # Agar arr[i] > arr[j], toh left side ke baki sab bhi bade honge
                temp_arr[k] = arr[j]
                inv_count += (mid - i + 1)
                j += 1
            k += 1
            
        # Bache huye elements copy karein
        while i <= mid:
            temp_arr[k] = arr[i]
            i += 1
            k += 1
        while j <= right:
            temp_arr[k] = arr[j]
            j += 1
            k += 1
            
        # Original array mein wapas copy karein
        for loop_var in range(left, right + 1):
            arr[loop_var] = temp_arr[loop_var]
            
        return inv_count
