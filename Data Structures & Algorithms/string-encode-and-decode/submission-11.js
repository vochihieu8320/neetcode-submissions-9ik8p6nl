class Solution {
    /**
     * @param {string[]} strs
     * @returns {string}
     */
    encode(strs) {    
        let results = ""

        for (let i = 0; i < strs.length; i++) {
            const currentString = strs[i];
            const stringLength = currentString.length;
            results += `${stringLength}#${currentString}`
        }

        return results
    }

    /**
     * @param {string} str
     * @returns {string[]}
     */
    decode(str) {
        let stringLength = '';
    let startString = false;
    const delimeter = "#"
    let subString = '';
    let results = []
    for (let i = 0; i < str.length; i++) { 
        const character = str[i];
        if (!startString) {
            if (character == delimeter) {
                stringLength = Number(stringLength);
                 if (stringLength == 0) {
                    results.push('')
                } else { 
                    startString = true;
                }
            } else {
                stringLength += character;
            }
            
            continue;
        }
       
       const validString = startString && stringLength > 0
       if (validString) {
           subString += character;
           stringLength -= 1;
       }
       
       const endOfString = startString & stringLength <= 0
       if (endOfString) {
          results.push(subString);
          stringLength = '';
          subString = '';
          startString = false;
          continue;   
       }
    }
    
    return results;
    }
}
