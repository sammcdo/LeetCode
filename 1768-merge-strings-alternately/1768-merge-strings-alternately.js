/**
 * @param {string} word1
 * @param {string} word2
 * @return {string}
 */
var mergeAlternately = function(word1, word2) {
    let dist = Math.max(word1.length, word2.length)

    let out = ""
    for (let i = 0; i < dist; i++) {
        if (i < word1.length) {
            out += word1.charAt(i);
        }
        if (i < word2.length) {
            out += word2.charAt(i);
        }
    }

    return out
};