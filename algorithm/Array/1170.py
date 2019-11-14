'''
1170. Compare Strings by Frequency of the Smallest Character
https://leetcode.com/contest/weekly-contest-151/problems/compare-strings-by-frequency-of-the-smallest-character/

Let's define a function f(s) over a non-empty string s, 
which calculates the frequency of the smallest character in s. 
For example, if s = "dcce" then f(s) = 2 because the smallest character 
is "c" and its frequency is 2.

Now, given string arrays queries and words, return an integer array answer, 
where each answer[i] is the number of words such that 
f(queries[i]) < f(W), where W is a word in words.

Example 1:
Input: queries = ["cbd"], words = ["zaaaz"]
Output: [1]
Explanation: 
On the first query we have f("cbd") = 1, f("zaaaz") = 3 so 
f("cbd") < f("zaaaz").

Example 2:
Input: queries = ["bbb","cc"], words = ["a","aa","aaa","aaaa"]
Output: [1,2]
Explanation: 
On the first query only f("bbb") < f("aaaa"). 
On the second query both f("aaa") and f("aaaa") are both > f("cc").

Constraints:

1 <= queries.length <= 2000
1 <= words.length <= 2000
1 <= queries[i].length, words[i].length <= 10
queries[i][j], words[i][j] are English lowercase letters.
'''
from typing import *
import collections

class Solution:
    def freq(self, str):
        counter = collections.Counter(str)
        c = min(str)
        return counter[c]

    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        fws = []
        for word in words:
            fws.append(self.freq(word))
        ans = []
        for query in queries:
            cnt = 0
            freQ = self.freq(query)
            for fw in fws:
                if freQ < fw:
                    cnt += 1
            ans.append(cnt)
        return ans

class SortingSolution:
    def frequency(self,str):
        if not str:
            return 0
        str = sorted(str)
        # After sorting, minmum at beginning
        minCharCnt=0
        for char in str:
            if char==str[0]:
                minCharCnt+=1
            else:
                break
        return minCharCnt

    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        answer = []
        fws = []
        for w in words:
            fws.append(self.frequency(w))
        for q in queries:
            count = 0
            fq = self.frequency(q)
            for fw in fws:
                if fw>fq:
                    count += 1
            answer.append(count)
        return answer

print(Solution().numSmallerByFrequency(queries = ["cbd"], words = ["zaaaz"]))
#[1]
print(Solution().numSmallerByFrequency(queries = ["bbb","cc"], words = ["a","aa","aaa","aaaa"]))
#[1,2]