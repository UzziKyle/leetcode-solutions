# EASY

# first submission
# runtime: 129 ms O(n)
# memory: 17.4 MB 
class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        num = 0
        nums.sort()
        length = len(nums)
        while num < length:
            if nums[num] != num:
                return num

            num +=  1

        return num
    
 
# second submission
# runtime: 129 ms O(n)
# memory: 17.6 MB    
class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        missing_num = 0
        nums.sort()
        for num in nums:
            if num != missing_num:
                return missing_num

            missing_num +=  1

        return missing_num