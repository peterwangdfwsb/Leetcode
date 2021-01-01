'''
	Given a string, find the length of the longest substring without repeating characters.

	Examples:

	Given "abcabcbb", the answer is "abc", which the length is 3.

	Given "bbbbb", the answer is "b", with the length of 1.

	Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        mapSet = {}
        start, result = 0, 0

        for end in range(len(s)):
        	if s[end] in mapSet:
        		start = max(mapSet[s[end]], start)
        	result = max(result, end-start+1)
        	mapSet[s[end]] = end+1

        return result 
        
'''
	There are two sorted arrays nums1 and nums2 of size m and n respectively.

	Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

	Example 1:
	nums1 = [1, 3]
	nums2 = [2]

	The median is 2.0
	Example 2:
	nums1 = [1, 2]
	nums2 = [3, 4]

	The median is (2 + 3)/2 = 2.5
'''

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        if len(nums1) > len(nums2):
        	nums1, nums2 = nums2, nums1

        x, y = len(nums1), len(nums2)
        low , high = 0, x

        while  low <= high:
        	partitionx = (low+high)/2
        	partitiony = (x+y+1)/2 - partitionx
        	if partitionx == 0:
        		maxLeftX = float('-inf')
        	else:
	        	maxLeftX = nums1[partitionx-1]

	        if partitionx == x:
	        	minRightX = float('inf')
	        else:
	        	minRightX = nums1[partitionx]

	        if partitiony == 0:
	        	maxLeftY = float('-inf')
	        else:
	        	maxLeftY = nums2[partitiony-1]

	        if partitiony == y:
	        	minRightY = float('inf')
	        else:
	        	minRightY = nums2[partitiony]

	        if maxLeftX <= minRightY and maxLeftY <= minRightX:
	        	if((x+y)%2 == 0):
	        		return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY))/2.0
	        	else:
	        		return max(maxLeftY, maxLeftX)
	        elif maxLeftX > minRightY:
	        	high = partitionx - 1
	        else:
	        	low = partitionx + 1


print Solution().findMedianSortedArrays([1,2], [3, 4])

'''
	Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

	Example 1:

	Input: "babad"
	Output: "bab"
	Note: "aba" is also a valid answer.
	Example 2:

	Input: "cbbd"
	Output: "bb"
'''

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
        maxLength, result = 1, ""
        for index in range(len(s)):
        	dp[index][index] = 1
        	result = s[index]

        length = 2
        
        while length <= len(s):
        	index_i = 0
        	while index_i < len(s) - length + 1:
        		index_j = index_i + length -1

        		if length == 2 and s[index_i] == s[index_j]:
        			dp[index_i][index_j] = 1
        			maxLength = max(maxLength, 2)
        			result = s[index_i:index_j+1]
        		elif s[index_i] == s[index_j] and dp[index_i+1][index_j-1]:
        			dp[index_i][index_j] = 1
        			if length > maxLength:
        				maxLength = length
        				result = s[index_i:index_j+1]

        		index_i += 1
        	length += 1

        return result

# Space: O(N^2)
# Time: O(N^2)

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        def expand(s, left, right):
        	while left >= 0 and right < len(s) and s[left] == s[right]:
        		left -= 1
        		right += 1
        	return right-left-1

        start, end = 0, 0
        for index in range(len(s)):
        	even_len = expand(s, index, index+1)
        	odd_len = expand(s, index, index)
        	length = max(even_len, odd_len)
        	if length > (end-start):
        		start = index - (length-1)/2
        		end = index +length/2

        return s[start:end+1]
       
'''
	The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

	P   A   H   N
	A P L S I I G
	Y   I   R

	And then read line by line: "PAHNAPLSIIGYIR"
'''

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        
        if numRows == 1:
        	return s

        result = ["" for _ in range(numRows)]
        row, down = 0, 1
        for char in s:
        	result[row] += char

        	if row == numRows - 1:
        		down = 0
        	if row == 0:
        		down = 1

        	if down:
        		row += 1
        	else:
        		row -= 1
        final_string = ""
        for value in result:
        	final_string += value
        return final_string

print Solution().convert("PAYPALISHIRING",3)
