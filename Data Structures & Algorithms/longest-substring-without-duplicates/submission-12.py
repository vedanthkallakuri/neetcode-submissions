class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        ans = 0
        ref = set()

        for i in range(len(s)):
            while s[r] in ref:
                ref.remove(s[l])
                l += 1
            ref.add(s[r])
            ans = max(ans, r - l + 1)
            r += 1
        
        return ans
            

