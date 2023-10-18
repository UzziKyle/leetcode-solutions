# EASY

# first submission
# runtime: 31 ms O(log n)
# memory: 16.1 MB 
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        answer = False
        while n > 1:
            if n % 2 != 0:
                break
            n /= 2

        if n == 1:
            answer = True

        return answer
    
    
# second submission (without loop)
# runtime: 47 ms O(1)
# memory: 16.21 MB 
# src: https://tutorialcup.com/leetcode-solutions/power-of-two-leetcode-solution.htm#AlgorithmTrivial
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
            
        return (n & (n - 1)) == 0