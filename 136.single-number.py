# EASY

# first submission
# runtime: 129 ms O(n)
# memory: 19 MB 
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        dict = {}
        for num in nums:
            if num in dict.keys():
                dict.pop(num)
                continue

            dict[num] = 1

        return dict.popitem()[0]
    
    
# second submission
# runtime: 124 ms O(n)
# memory: 18.8 MB 
# src: https://medium.com/@punitkmr/single-number-fe30e4f6693d
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        dict = {}
        for num in nums:
            try:
                dict.pop(num)
            except:
                dict[num] = 1

        return dict.popitem()[0]
    
    
# third submission
# runtime: 128 ms O(n)
# memory: 19 MB 
# src: https://medium.com/@punitkmr/single-number-fe30e4f6693d
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        return (2 * sum(set(nums))) - sum(nums)
    
    
# fourth submission
# runtime: 771 ms O(n^2)
# memory: 19.1 MB 
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        numlist = []
        for num in nums:
            if num in numlist:
                numlist.remove(num)
                continue

            numlist.append(num)

        return numlist[0]
    
    
# fifth submission
# runtime: 128 ms O(n)
# memory: 18.8 MB 
# src: https://medium.com/@punitkmr/single-number-fe30e4f6693d
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        single_num = 0
        for num in nums:
            single_num ^= num

        return single_num 
    
    
# sixth submission
# runtime: 137 ms O(n)
# memory: 18.6 MB 
# src: https://dzone.com/articles/optimal-solution-single-number-leetcode-problem
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        nums.sort()
        idx = 0
        while idx < len(nums) - 2:
            if nums[idx] != nums[idx + 1]:
                return nums[idx]

            idx += 2

        return nums[idx]