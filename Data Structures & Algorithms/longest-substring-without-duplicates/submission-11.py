class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        p, ans, run = 0, 0, 0
        ref = {}

        while p < len(s):
            if s[p] in ref:
                ans = max(ans, run)
                p = ref[s[p]] + 1
                run = 0
                ref.clear()                
            else:
                ref[s[p]] = p
                run += 1
                p += 1

        return max(ans, run)

