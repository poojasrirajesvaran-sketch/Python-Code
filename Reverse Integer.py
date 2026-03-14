class Solution:
    def reverse(self, x: int) -> int:
        # Define 32-bit signed integer boundaries
        MIN_INT, MAX_INT = -2**31, 2**31 - 1
        
        res = 0
        # Determine sign and work with absolute value
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        while x != 0:
            digit = x % 10
            x //= 10
            
            # Check for overflow before multiplying by 10
            # If res > MAX_INT // 10, the next step will overflow
            if res > MAX_INT // 10:
                return 0
            
            res = res * 10 + digit
            
        res *= sign
        
        # Final boundary check (mostly for the -2^31 edge case)
        if res < MIN_INT or res > MAX_INT:
            return 0
            
        return res
