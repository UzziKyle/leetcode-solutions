# EASY

# first submission
# runtime: 61 ms O(n)
# memory: 16.2 MB
class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x = str(x)
        if str_x == str_x[::-1]:
            return True

        return False
    

# second submission
# runtime: 59 ms O(n)
# memory: 16.3 MB
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]
    
    
# third submission, "learned" from the internet
# runtime: 63 ms O(n)
# memory: 16.2 MB
class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = x
        rev = 0
        while x > 0:
            dig = x % 10
            rev = rev * 10 + dig
            x //= 10

        return temp == rev