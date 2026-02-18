# You are given an array arr of positive integers. Your task is to find all the leaders in the array. An element is considered a leader if it is greater than or equal to all elements to its right. 
# The rightmost element is always a leader.


class Solution:
    def leaders(self, arr):
        n = len(arr)
        res = []
        
        # Rightmost element hamesha leader hota hai
        max_from_right = arr[n-1]
        res.append(max_from_right)
        
        # Piche se loop chalayein (n-2 se 0 tak)
        for i in range(n-2, -1, -1):
            if arr[i] >= max_from_right:
                max_from_right = arr[i]
                res.append(max_from_right)
        
        # Result ko seedha karne ke liye reverse karein
        return res[::-1]
