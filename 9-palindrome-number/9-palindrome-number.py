class Solution:
    def isPalindrome(self, x: int) -> bool:
        xstr = str(x)
        if xstr[::-1] == xstr:
            return True
        else:
            return False
