class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        substr = ""
        for c in s:
            if not c in substr:
                substr += c
            else:
                ans = len(substr) if len(substr) > ans else ans
                substr = substr[substr.find(c) + 1:] + c

        ans = len(substr) if len(substr) > ans else ans
        return ans

a = Solution()
print(a.lengthOfLongestSubstring("aabaab!bb"))
