class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)

        result = []
        result_hash = {}

        for i in range(n):
            target = nums[i] * -1
            left = 0;
            right = n - 1
            
            while left < right:
                if left == i: left += 1; continue;
                if right == i: right -= 1; continue;
            
                sum = nums[left] + nums[right];

                if sum > target: right -= 1;
                elif sum < target: left += 1;
                elif sum == target:
                    key_arrays = [nums[i], nums[left], nums[right]]
                    key_arrays.sort()
                    key = f"key_#{key_arrays[0]}_#{key_arrays[1]}_#{key_arrays[2]}"
                    if result_hash.get(key) is None:
                        result_hash[key] = True
                        result.append([nums[i], nums[left], nums[right]])

                    left+=1;

        return result
        