class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<=0:
            return False
        if n==1:
            return True
        k = log(n)/log(4)
        return 4**(floor(k))==n or 4**(ceil(k))==n
