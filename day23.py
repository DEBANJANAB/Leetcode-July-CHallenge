class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        res=dict()
        for i in nums:
            if i not in res:
                res[i]=1
            else:
                res.pop(i)
        return res        
