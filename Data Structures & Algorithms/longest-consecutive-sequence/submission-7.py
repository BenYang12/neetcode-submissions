class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # nums -> return length of longest consecutive sequence
        # to avoid repeatedly recounting same sequences, only start counting at beginning of consecutive sequence. 

        # use a set
        # start of sequence -> num - 1 is not in the set
        # once we identify such a starting number, keep checking if num + 1, num + 2 exist in the set and go afap
        # nums = [2,20,4,10,3,4,5] -> (2, 20, 4, 10, 3, 5)

        numSet = set(nums)
        res = 0
        for num in numSet:
            if num - 1 not in numSet:
                # start of sequence
                count = 1
                while num + count in numSet:
                    count += 1
                res = max(res, count)
        return res


        



        