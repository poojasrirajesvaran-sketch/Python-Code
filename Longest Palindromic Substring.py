class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        start, end = 0, 0
        
        def expandAroundCenter(left: int, right: int) -> int:
            # Expand as long as pointers are in bounds and chars match
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Return the length of the palindrome found
            return right - left - 1

        for i in range(len(s)):
            # Check for odd length (e.g., "aba")
            len1 = expandAroundCenter(i, i)
            # Check for even length (e.g., "abba")
            len2 = expandAroundCenter(i, i + 1)
            
            curr_max = max(len1, len2)
            
            # If we found a longer one, update our boundaries
            if curr_max > end - start:
                start = i - (curr_max - 1) // 2
                end = i + curr_max // 2
                
        return s[start : end + 1]
