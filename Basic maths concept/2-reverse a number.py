class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1  #to handle -ve numbers
        x = abs(x)
        revn = 0

        while x > 0:
            revn = revn * 10 + x % 10
            x //= 10

        revn *= sign

        if revn < -2**31 or revn > 2**31 - 1:
            return 0

        return revn
