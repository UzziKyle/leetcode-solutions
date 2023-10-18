# EASY

# first submission (using Python dict)
# runtime: 45 ms 
# memory: 16.2 MB 
class Solution:
    def isHappy(self, n: int) -> bool:
        hashdict = {}
        while True:
            if n == 1:
                return True

            str_num = str(n)
            n = 0
            for num in str_num:
                n += int(num) ** 2

            if n in hashdict:
                return False

            hashdict[n] = 1
            
            
# second submission (using Python set)
# runtime: 42 ms 
# memory: 16.3 MB
class Solution:
    def isHappy(self, n: int) -> bool:
        numset = set()
        while True:
            if n == 1:
                return True

            str_num = str(n)
            n = 0
            for num in str_num:
                n += int(num) ** 2

            if n in numset:
                return False

            numset.add(n) 