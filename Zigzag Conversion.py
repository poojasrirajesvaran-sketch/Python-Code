class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # If there's only one row, the zigzag is just the original string
        if numRows == 1 or numRows >= len(s):
            return s
        
        # Create a list of strings, one for each row
        rows = [""] * numRows
        curr_row = 0
        direction = -1 # Starts at -1 because we flip it to 1 immediately
        
        for char in s:
            rows[curr_row] += char
            
            # If we are at the top or bottom row, reverse the direction
            if curr_row == 0 or curr_row == numRows - 1:
                direction *= -1
                
            curr_row += direction
            
        # Join all rows together to get the final string
        return "".join(rows)
