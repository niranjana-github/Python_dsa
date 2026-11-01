class Solution:
    def reverseString(self, s: str) -> str:
        l=0
        r=len(s)-1
        s=list(s)
        while l<r:
            s[l],s[r]=s[r],s[l]
            l+=1
            r-=1
        reversed=''
        for ch in s:
            reversed+=ch
        return reversed
             
