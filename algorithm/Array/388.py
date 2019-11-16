'''
388. Longest Absolute File Path
https://leetcode.com/problems/longest-absolute-file-path/

Suppose we abstract our file system by a string in the following manner:
The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" represents:
dir
    subdir1
        file1.ext
        subsubdir1
    subdir2
        subsubdir2
            file2.ext
Given a string representing the file system in the above format,
return the length of the longest absolute path to file in the abstracted file system.
If there is no file in the system, return 0.

Note:
The name of a file contains at least a . and an extension.
The name of a directory or sub-directory will not contain a ..
Time complexity required: O(n) where n is the size of the input string.
Notice that a/aa/aaa/file1.txt is not the longest file path,
if there is another path aaaaaaaaaaaaaaaaaaaaa/sth.png.
'''
class Solution:
    def lengthLongestPath(self, input: str) -> int:
        maxlen = 0
        pathlen = {0: 0}
        # Split string by '\n', here can use splitlines()
        for line in input.splitlines():
            # Remove ALL '\t' in the left
            name = line.lstrip('\t')
            # Get how deep by number of '\t' removed !
            depth = len(line) - len(name)
            if '.' in name:
                maxlen = max(maxlen, pathlen[depth] + len(name))
            else:
                # Update the depth for in-folder files or sub-folder
                pathlen[depth + 1] = pathlen[depth] + len(name) + 1
        return maxlen

print(Solution().lengthLongestPath("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"))
#dir
#   subdir1
#       file1.ext
#       subsubdir1
#   subdir2
#       subsubdir2
#           file2.ext
#dir/subdir2/subsubdir2/file2.ext => 32

print(Solution().lengthLongestPath("dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"))
#dir
#    subdir1
#    subdir2
#        file.ext
#dir/subdir2/file.ext => 20

print(Solution().lengthLongestPath("dir\n\twhat_a_long_file_abcdefghijkl.ext\n\tlevel1_file.ext\n\tsubdir1_long_path\n\tsubdir2\n\t\tfile.ext\n\t\ta.ext"))
#dir
#    what_a_long_file_abcdefghijkl.ext
#    level1_file.ext
#    subdir1_long_path
#    subdir2_short
#        file.ext
#        a.ext
#dir/what_a_long_file_abcdefghijkl.ext => 37