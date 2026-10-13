class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # nums -> return length of longest consecutive sequence
        # to avoid repeatedly recounting same sequences, only start counting at beginning of consecutive sequence. 

        # start of sequence -> num - 1 is not in the set
        # once we identify such a starting number, keep checking if num + 1, num + 2 exist in the set and go afap
        # (2, 20, 4, 10, 3, 5)

        numSet = set(nums)
        longest = 0

        for num in numSet:
            # start of sequence identified
            if (num - 1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                longest = max(longest, length)
        return longest



        