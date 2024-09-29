"""
Given a string s, find the length of the longest
substring without repeating characters.


Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""

class Solution:
    def length_of_longest_substring(self, s: str) -> int:

        if len(s) < 2:
            return len(s)

        max_length = 0
        queue = []
        qset = set()

        cur_length = 0
        for character in s:
            if character in qset:
                while queue[0] != character:
                    qset.remove(queue.pop(0))
                queue.pop(0)
                queue.append(character)
                cur_length = len(queue)
            else:
                queue.append(character)
                qset.add(character)
                cur_length += 1
            max_length = max(cur_length, max_length)

        return max_length


