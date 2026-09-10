class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        maxLen = 0
        resultSet = set()
        for right in range(len(s)):
            while s[right] in resultSet: #if duplicate is found slide the window forward from left and update
                resultSet.remove(s[left]) # slide the window one place forward from left
                left += 1
            resultSet.add(s[right]) # Add the current element and update maxLen
            maxLen = max(maxLen, right-left + 1)# maxLength is the size of the current window vs maxLength
        print(resultSet)
        return maxLen
        