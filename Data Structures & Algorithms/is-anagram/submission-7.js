class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    hashString(s) {
        let results = {};
        for (let i = 0; i < s.length; i++) {
            const value = s[i];
            if (results[value] == null) {
                results[value] = 1;
            } else {
                results[value] = results[value] + 1;
            }
        }

        return results;
    }

    isAnagram(s, t) {
        if (s.length != t.length) return false;
    
       let hashT = this.hashString(t);

       for(let i = 0; i < s.length; i++) {
            const value = s[i];
            if (hashT[value] == null || hashT[value] <= 0) { 
                return false;
            } else {
                hashT[value] = hashT[value] - 1
            }
       }

       return true
    }
}
