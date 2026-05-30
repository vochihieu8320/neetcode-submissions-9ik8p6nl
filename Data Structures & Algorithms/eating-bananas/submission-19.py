import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        right = max(piles)
        left = 1

        print("right", right)
        print("left", left)

        while left < right:
            mid = (right + left) // 2
            total_hour = sum(math.ceil(pile / mid) for pile in piles)
            if total_hour > h:
                left = mid + 1
            else:
                right = mid

        return right
       
        