class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        haveSeen = []
        
        for n in nums:
            if n in haveSeen:
                return True
            haveSeen.append(n)

        return False

        