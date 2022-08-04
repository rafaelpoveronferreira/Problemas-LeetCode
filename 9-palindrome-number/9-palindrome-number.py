class Solution:
    # First solution: converting to string
    def isPalindromestr(self, x: int) -> bool:
        xstr = str(x)
        return (xstr[::-1] == xstr)
    
    # Second solution: without converting to string
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        reversedx = 0
        while (x > reversedx):
            reversedx = (x % 10) + reversedx*10
            x = int(x/10)
        
        return x == reversedx or (x == int(reversedx/10))
