/**
 * 49. Group Anagrams (Medium)
 *
 * Given an array of strings strs, group the anagrams together. You can return the
 * answer in any order.
 *
 * An Anagram is a word or phrase formed by rearranging the letters of a different
 * word or phrase, typically using all the original letters exactly once.
 *
 * Constraints:
 *
 *   1 <= strs.length <= 104
 *   0 <= strs[i].length <= 100
 *   strs[i] consists of lowercase English letters.
 */

/**
 * Patterns: Arrays, Hashing, Strings
 * Time: O(n^2) where n is the number of strings.
 * Space: O(n+n) where n is the number of strings.
 *
 * Iterate over each string and create an array of lowercase letter (a-z)
 * counts. Convert this array into a key that represents the letters and
 * counts. Anagrams will produce the same key as they have the same letters
 * and counts. Use this key to group to the strings into groups.
 *
 * @param {string[]} strs the strings to group into anagrams.
 * @return {string[][]} an array of anagram groups.
 */
var groupAnagrams = function (strs) {
  const strCounts = {};
  for (const str of strs) {
    const counts = new Array(26).fill(0);
    for (let i = 0; i < str.length; i++) {
      const code = str.charCodeAt(i) - "a".charCodeAt(0);
      counts[code]++;
    }
    strCounts[str] = counts;
  }

  const groups = {};
  for (const [str, counts] of Object.entries(strCounts)) {
    const key = JSON.stringify(counts);
    if (key in groups) {
      groups[key].push(str);
    } else {
      groups[key] = [str];
    }
  }

  return Object.values(groups);
};

test("example 1", () => {
  const strs = ["eat", "tea", "tan", "ate", "nat", "bat"];
  const ans = groupAnagrams(strs);
  expect(ans).toEqual([["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]);
});

test("example 2", () => {
  const strs = [""];
  const ans = groupAnagrams(strs);
  expect(ans).toEqual([[""]]);
});

test("example 3", () => {
  const strs = ["a"];
  const ans = groupAnagrams(strs);
  expect(ans).toEqual([["a"]]);
});
