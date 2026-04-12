class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        let results = {};

        for (let i = 0; i < strs.length; i++) {
            const value = strs[i];
            const sortedValue = value.split("").sort();

            if (results[sortedValue] != null) {
                results[sortedValue].push(value)
            } else {
                results[sortedValue] = [value]
            }

        }

        return Object.values(results)
    }
}
