class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}  # Tracks the last index of each character
        max_length = 0
        start = 0      # Left boundary of the window
        
        for end in range(len(s)):
            # If char is a duplicate AND inside the current window
            if s[end] in char_map and char_map[s[end]] >= start:
                # Jump 'start' to the right of the previous occurrence
                start = char_map[s[end]] + 1
            
            # Update last seen index of the character
            char_map[s[end]] = end
            
            # Update the max length found so far
            max_length = max(max_length, end - start + 1)
            
        return max_length
