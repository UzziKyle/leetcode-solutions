# EASY

# first submission
# runtime: 42 ms O(n)
# memory: 17.1 MB 
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(filter(str.isalnum, s.lower()))

        return s == s[::-1]