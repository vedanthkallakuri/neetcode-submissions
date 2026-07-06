class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,r = 0,0
        freq = {}
        ans = 0
        while r < len(s):
            freq[s[r]] = freq.get(s[r], 0) + 1

            max_freq = 0
            for f in freq.values():
                max_freq = max(f, max_freq)
        
            while (r-l+1) - max_freq > k:
                freq[s[l]] -= 1
                l += 1
                
                max_freq = 0
                for f in freq.values():
                    max_freq = max(f, max_freq)
            
            ans = max(r-l+1, ans)
            r += 1
            
        return ans
