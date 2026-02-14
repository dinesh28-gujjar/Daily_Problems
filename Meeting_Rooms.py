# Given a 2D array arr[][], where arr[i][0] is the starting time of ith meeting and arr[i][1] is the ending time of ith meeting, 
# the task is to check if it is possible for a person to attend all the meetings such that he can attend only one meeting at a particular time.
# Note: A person can attend a meeting if its starting time is greater than or equal to the previous meeting's ending time.




class Solution:
    def canAttend(self, arr):
        # If 0 or 1 meeting, always possible
        if len(arr) <= 1:
            return True

        # Sort meetings based on starting time
        arr.sort(key=lambda x: x[0])

        # Check for overlap
        for i in range(len(arr) - 1):
        # If next meeting starts before current meeting ends
            if arr[i + 1][0] < arr[i][1]:
                return False

        return True
