class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return (x for i in range(len(nums)+1) for x in combinations(nums,i))
        
