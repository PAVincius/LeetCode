class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = {}
        for i in range(len(nums)):
            df = target - nums[i]
            if df in index:
                return [index[df],i]
            else:
                index[nums[i]] = i