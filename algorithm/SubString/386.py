'''
386. Longest Substring with At Most K Distinct Characters
https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/
https://www.lintcode.com/problem/longest-substring-with-at-most-k-distinct-characters

Hi, here's your problem today. This problem was recently asked by Amazon:
You are given a string s, and an integer k. 
Return the length of the longest substring in s that contains at most k distinct characters.
For instance, given the string:
aabcdefff and k = 3, then the longest substring with 
3 distinct characters would be defff. 
The answer should be 5.
Challenge: O(n) time

Longest sequence just contains 2 unique numbers

Hi, here's your problem today. This problem was recently asked by Facebook:
Given a sequence of numbers, find the longest sequence that contains only 2 unique numbers.
Example:
Input: [1, 3, 5, 3, 1, 3, 1, 5]
Output: 4
The longest sequence that contains just 2 unique numbers is [3, 1, 3, 1]
'''
class Solution:
    """
    @param s: A string
    @param k: An integer
    @return: An integer
    """
    def lengthOfLongestSubstringKDistinct(self, s, k):
        maxLength = 0
        charDict = {}
        left = 0
        for idx in range(len(s)):
            charDict[s[idx]] = idx
            while len(charDict)>k:
                if charDict[s[left]] == left:
                    del charDict[s[left]]
                left += 1
            maxLength = max(maxLength, idx - left + 1)
        return maxLength
    def findSequence(self, seq):
        maxSequence, left = 0, 0
        dict = {}
        for i,s in enumerate(seq):
            dict[s] = i #We only need to keep last appear of s
            while len(dict) > 2:
                if dict[seq[left]] == left: #if seq[left] not duplicate
                    del dict[seq[left]]
                left += 1
            maxSequence = max(maxSequence, i - left + 1)
        return maxSequence

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

class TestLongestSequence(unittest.TestCase):

    def testExample1(self):
        n = Solution().findSequence([1, 3, 5, 3, 1, 3, 1, 5])
        #Explanation: [3, 1, 3, 1]
        self.assertEqual(n, 4)

    def testBoundary(self):
        n = Solution().findSequence([1, 3, 3, 3, 3, 3, 1, 3])
        #Explanation: all
        self.assertEqual(n, 8)
        n = Solution().findSequence([1, 2, 3, 4, 5, 6, 7, 8])
        #Explanation: pairs
        self.assertEqual(n, 2)
        n = Solution().findSequence([1, 2, 3, 1, 1, 1, 1, 8])
        #Explanation: [3, 1, 1, 1, 1]
        self.assertEqual(n, 5)

if __name__ == "__main__":
    unittest.main()