'''
386. Longest Substring with At Most K Distinct Characters
https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/
https://www.lintcode.com/problem/longest-substring-with-at-most-k-distinct-characters

Hi, here's your problem today. This problem was recently asked by Amazon:

You are given a string s, and an integer k. Return the length of the longest substring in s that contains at most k distinct characters.

For instance, given the string:
aabcdefff and k = 3, then the longest substring with 3 distinct characters would be defff. The answer should be 5.

Challenge: O(n) time
'''
class Solution:
    """
    @param s: A string
    @param k: An integer
    @return: An integer
    """
    def lengthOfLongestSubstringKDistinct(self, s, k):
        length = 0
        charDict = {}
        drop = 0
        for idx in range(len(s)):
            if s[idx] not in charDict:
                charDict[s[idx]] = 1
            else:
                charDict[s[idx]] += 1

            while len(charDict)>k:
                if charDict[s[drop]] == 1:
                    del charDict[s[drop]]
                else:
                    charDict[s[drop]] -= 1
                drop += 1

            length = max(length, 1+idx-drop)
        return length

import unittest

class TestLongestSubstring(unittest.TestCase):

    def testExample1(self):
        n = Solution().lengthOfLongestSubstringKDistinct("eceba",3)
        #Explanation: T = "eceb"
        self.assertEqual(n, 4)

    def testExample2(self):
        n = Solution().lengthOfLongestSubstringKDistinct("WORLD",4)
        #Explanation: T = "WORL" or "ORLD"
        self.assertEqual(n, 4)

    def testExample3(self):
        n = Solution().lengthOfLongestSubstringKDistinct("aabcdefff",3)
        #because 'defff' has length 5 with 3 characters
        self.assertEqual(n, 5)

    def testNonAlphaical(self):
        n = Solution().lengthOfLongestSubstringKDistinct("a   $    a",3)
        self.assertEqual(n, 10)

    def testLessThanK(self):
        n = Solution().lengthOfLongestSubstringKDistinct("a        a",3)
        self.assertEqual(n, 10)

    def testEmptyString(self):
        n = Solution().lengthOfLongestSubstringKDistinct("",3)
        self.assertEqual(n, 0)

    def testBoundary(self):
        n = Solution().lengthOfLongestSubstringKDistinct("ab",1)
        self.assertEqual(n, 1)
        n = Solution().lengthOfLongestSubstringKDistinct("abc",2)
        self.assertEqual(n, 2)
        n = Solution().lengthOfLongestSubstringKDistinct("ababababaa",1)
        self.assertEqual(n, 2)
        n = Solution().lengthOfLongestSubstringKDistinct("abbbababba",1)
        self.assertEqual(n, 3)

if __name__ == "__main__":
    unittest.main()