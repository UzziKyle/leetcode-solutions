# EASY

# first submission
# runtime: 39 ms
# memory: 16.3 MB
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        while True:
            if val in nums:
                nums.remove(val)

            if val not in nums:
                break

        return len(nums)
    
    
# second submission
# runtime: 47 ms
# memory: 16.1 MB
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        for idx in range(len(nums) - 1, -1, -1):
            if nums[idx] == val:
                nums.pop(idx)

        return len(nums)
    

# third submission
# runtime: 32 ms
# memory: 16.3 MB
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = len(nums)
        for idx in range(k - 1, -1, -1):
            if nums[idx] == val:
                nums.pop(idx)
                k -= 1

        return k