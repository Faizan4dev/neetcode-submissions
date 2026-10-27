class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            needed = target - nums[i]
            if needed not in seen:
                seen[nums[i]] = i
            else:
                return [seen[needed] , i]