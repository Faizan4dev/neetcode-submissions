class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = 0
        maj = nums[0]

        for num in range(len(nums)):
            if nums[num] == maj:
                freq +=1
            else:
                freq -=1
            
            if freq ==0:
                maj = nums[num]
                freq +=1
            
        return maj
            


