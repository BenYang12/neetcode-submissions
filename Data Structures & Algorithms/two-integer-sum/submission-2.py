class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {} #value:idx

        for i, num in enumerate(nums):
            diff = target - num
            if diff in hashMap:
                return [hashMap.get(diff), i]
            else:
                hashMap[num] = i


        