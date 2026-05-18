class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        r = 0
        
        ref = {}
        ans = 0
        run = 0
        while r < len(s):
            if s[r] in ref:
                ans = max(ans, run)
                run = 0
                r = ref[s[r]] + 1
                ref.clear()
                print(ref)
                
            else:
                ref[s[r]] = r
                run += 1
                r += 1
        return max(ans, run)

