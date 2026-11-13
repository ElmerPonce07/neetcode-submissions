class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seenBefore = {}

        for i in range(len(nums)):
            curr = nums[i]
            missNum = target - curr

            if  missNum in seenBefore:
                return [seenBefore[missNum], i]

            seenBefore[curr] = i
            
        return []

        