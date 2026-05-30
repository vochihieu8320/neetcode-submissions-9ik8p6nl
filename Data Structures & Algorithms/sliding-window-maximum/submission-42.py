from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        n = len(nums)
        result = []
        left = 0

        for right in range(n):
            while dq and nums[dq[-1]] <= nums[right]:
                dq.pop()

            dq.append(right)

            if dq[0] < left:
                dq.popleft()

            if right - left + 1 == k:
                result.append(nums[dq[0]])
                left += 1

        return result

        