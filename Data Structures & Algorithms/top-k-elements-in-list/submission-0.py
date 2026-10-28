class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums)+1)]
        for i in range(len(nums)):
            if nums[i] not in count:
                count[nums[i]] = 1
            else:
                count[nums[i]] +=1
        
        # print(freq)
        for n,f in count.items():
            freq[f].append(n)
        
        res = []
        for j in range(len(freq)-1 , 0 ,-1):
            if freq[j]:
                for num in freq[j]:
                    res.append(num)
                    if len(res) == k :
                     return res
            

        
