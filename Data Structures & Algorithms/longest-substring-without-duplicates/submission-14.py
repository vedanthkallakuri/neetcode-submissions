class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, ans = 0, 0
        ref = {}

        for r in range(len(s)):
            if s[r] in ref:
                l = max(l, ref[s[r]] + 1)
            ref[s[r]] = r
            ans = max(ans, r - l + 1)
        
        return ans
            

    # l = 0, r = 0 > a 0 : 1
    # l = 0, r = 1 > b 1 : 2
    # l = 0, r = 2 > b 2 : max(2, 1)
    # l = 2, r = 3 > a 3 : max(2, 2)

