class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0;
        n = len(heights)
        right = n - 1
        max_container = 0

        while left < right:
            width = right - left
            height = min([heights[left], heights[right]])
            container = width * height
            max_container = container if container > max_container else max_container

            if heights[right] > heights[left]:
                left += 1
            else:
                right -= 1

        return max_container

        
        