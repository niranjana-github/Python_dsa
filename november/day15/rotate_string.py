class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        curr_string=s
        for i in range(len(s)):
            curr_string=curr_string[1:]+curr_string[0]
            if curr_string==goal:
                return True
        return False
s=Solution()
print(s.rotateString("abcde","cdeab"))
