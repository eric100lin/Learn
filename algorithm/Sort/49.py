'''
49. Group Anagrams
https://leetcode.com/problems/group-anagrams/

Hi, here's your problem today. This problem was recently asked by AirBNB:

Given a list of words, group the words that are anagrams of each other. 
(An anagram are words made up of the same letters).

Example:

Input: ['abc', 'bcd', 'cba', 'cbd', 'efg']
Output: [['abc', 'cba'], ['bcd', 'cbd'], ['efg']]

Note:
All inputs will be in lowercase.
The order of your output does not matter.
'''
#Ugly sort O(nklogk) solution...
def groupAnagramWordsUgly(strs):
    dict = {}
    for str in strs:
        #Need to use hashable data type as key!!
        #1. Use string
        #chsKey = "".join(sorted(str))
        #2. Use tuple
        chsKey = tuple(sorted(str))
        #3. Can not use set (NOT HASHABLE)
        # XX chsKey = set(str)
        #4. Can not use list (NOT HASHABLE)
        # XX chsKey = sorted(str)
        if chsKey in dict:
            dict[chsKey].append(str)
        else:
            dict[chsKey] = [ str ]
    result = []
    for chsKey in dict:
        result.append(dict[chsKey])
    return result

#Concise sort O(nklogk) solution!
import collections
def groupAnagramWordsSort(strs):
    dict = collections.defaultdict(list)
    for str in strs:
        dict[tuple(sorted(strs))].append(str)
    return list(dict.values())  #dict_values to list

#Count O(nk) solution!
def groupAnagramWords(strs):
    dict = collections.defaultdict(list)
    for str in strs:
        count = [0]*26
        for c in str:
            count[ord(c)-ord('a')] += 1
        dict[tuple(count)].append(str)
    return list(dict.values())  #dict_values to list

print(groupAnagramWords(['abc', 'bcd', 'cba', 'cbd', 'efg']))
# [['efg'], ['bcd', 'cbd'], ['abc', 'cba']]

print(groupAnagramWords(["eat","tea","tan","ate","nat","bat"]))
# [["bat"],["nat","tan"],["ate","eat","tea"]]
