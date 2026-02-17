# You are given an array arr[] of non-negative numbers. Each number tells you the maximum number of steps you can jump forward from that position.
# For example: If arr[i] = 3, you can jump to index i + 1, i + 2, or i + 3 from position i.
# If arr[i] = 0, you cannot jump forward from that position.
# Your task is to find the minimum number of jumps needed to move from the first position in the array to the last position.
# Note:  Return -1 if you can't reach the end of the array.


class Solution:
    def minJumps(self, arr):
        n = len(arr)
        
        # Agar pehla element 0 hai, toh aage nahi badh sakte
        if n <= 1: return 0
        if arr[0] == 0: return -1
        
        max_reach = arr[0]
        steps = arr[0]
        jumps = 1
        
        for i in range(1, n - 1):
            # Check karte hain ki current position se max kahan tak ja sakte hain
            max_reach = max(max_reach, i + arr[i])
            
            # Ek step kam ho gaya
            steps -= 1
            
            # Agar steps khatam ho gaye
            if steps == 0:
                jumps += 1
                
                # Agar hum current position se aage hi nahi badh pa rahe
                if i >= max_reach:
                    return -1
                
                # Agle jump ke liye steps update karein
                steps = max_reach - i
                
        return jumps
