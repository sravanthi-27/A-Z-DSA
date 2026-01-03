class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        revn = 0
        n = x
        while n>0:
            lastdigit = n%10
            n = n//10
            revn = (revn*10)+lastdigit
        if x==revn:
            return True
        else:
            return False
        
        