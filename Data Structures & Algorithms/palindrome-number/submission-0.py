class Solution:
    def isPalindrome(self, x: int) -> bool:
        xString=str(x)
        l,r=0,len(xString)-1

        while l<r:
            if xString[l]!=xString[r]:
                return False
            l+=1
            r-=1
        return True
        
            