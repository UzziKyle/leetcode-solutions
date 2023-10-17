# EASY

# first submission
# runtime: 79ms O(n)
# memory: 17.53 MB   
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        n = len(nums) - 1
        for idx in range(n, 0, -1):
            if nums[idx] == nums[idx - 1]:
                nums.pop(idx)

        return len(nums)
        
        
# second submission
# runtime: 76 ms O(n)
# memory: 17.70 MB          
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        idx = len(nums) - 1
        while idx > 0:
            if nums[idx] == nums[idx - 1]:
                nums.pop(idx)
            idx -= 1

        return len(nums)