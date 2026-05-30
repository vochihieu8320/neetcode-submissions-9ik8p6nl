class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        max_area = 0

        for i in range(n):
            min_height = heights[i]

            for j in range(i, n):
                min_height = min(min_height, heights[j])
                distance = j - i + 1
                window_area = distance * min_height
                max_area = max(max_area, window_area)


        return max_area

