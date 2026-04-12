class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        if (!nums) return [];
        if (nums.length <= 0) return [];

        let results = {};
        for (let i = 0; i < nums.length; i++) {
            const value = nums[i];
            const subtractValue = target - value;

            if (results[subtractValue] != null) {
                return [results[subtractValue], i]
            } else {
                results[value] = i
            }
        }

        return []
    }
}
