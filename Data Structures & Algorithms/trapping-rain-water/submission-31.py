class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        max_water = 0;

        for i in range(0, n):
            left = i
            right = left
            max_right = 0

            print("index", i);
            # find max right
            while right < n:
                max_right = height[right] if height[right] > max_right else max_right
                right += 1

            # find max left

            max_left = 0
            while left >= 0:
                max_left = height[left] if height[left] > max_left else max_left
                left -= 1

            print("max left", max_left)
            print("max right", max_right)
            water = min([max_left, max_right]) - height[i]


            if water > 0: max_water += water

        return max_water

