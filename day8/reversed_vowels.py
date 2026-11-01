class Solution:
    def modify(self, s):
        vowels='aeiou'
        l=0
        r=len(s)-1
        s=list(s)
        while l<r:
            if s[l] not in vowels:
                l+=1
            elif s[r] not in vowels:
                r-=1
            else:
                s[l],s[r]=s[r],s[l]
                l+=1
                r-=1
                
        reversed=''
        for ch in s:
            reversed+=ch
        return reversed
