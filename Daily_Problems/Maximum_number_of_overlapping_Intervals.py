# You are given an array of intervals arr[][], where each interval is represented by two integers [start, end] (inclusive). 
# Return the maximum number of intervals that overlap at any point in time.



class Solution:
    def overlapInt(self, arr):
        starts = []
        ends = []

        # split start & end
        for l, r in arr:
            starts.append(l)
            ends.append(r)

        # sort timelines
        starts.sort()
        ends.sort()

        n = len(arr)
        i = 0   # pointer for starts
        j = 0   # pointer for ends

        current = 0
        answer = 0

        # traverse timeline
        while i < n and j < n:
            # inclusive intervals: start <= end means overlap
            if starts[i] <= ends[j]:
                current += 1
                answer = max(answer, current)
                i += 1
            else:
                current -= 1
                j += 1

        return answer
