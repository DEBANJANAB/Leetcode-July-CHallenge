class Solution:
    def climbStairs(self, n: int) -> int:
        return round((0.5+sqrt(5)/2)**(n+1)/sqrt(5))
        
