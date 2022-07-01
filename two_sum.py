class Solution:
    """this code allowed me to achieve, as of 01/07/2022:
    for strategy #1:
        Runtime: 58 ms, faster than 97.95% of Python3 online submissions for Two Sum.
        Memory Usage: 15.2 MB, less than 24.33% of Python3 online submissions for Two Sum.
    for strategy #2:
        Runtime: 723 ms, faster than 33.73% of Python3 online submissions for Two Sum.
        Memory Usage: 14.8 MB, less than 99.47% of Python3 online submissions for Two Sum.
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        :param nums:
        :param target:
        :return:
        Given an array of integers nums and an integer target, return indices of the two numbers such that they add up
        to target.
        You may assume that each input would have exactly one solution, and you may not use the same element twice.
        You can return the answer in any order.

        Strategy:
        #1. Time-optimized:
        - create a dictionary where the keys are the numbers for which the check has been performed,
        where the values are their indexes
        - for each index-value pair of the nums list compute the difference between the target and the current value
        - look up the difference in the dictionary keys
        - - if it's present return the current index and the index corresponding to the difference
        - - if it's not present add the current index to the dictionary using the difference as key
        #2. Memory-optimized:
        Sequentually check the sum of every element with the subsequents and return the two indices
        when the it's equal to the given target, return False if the two nested loops finish
        """

# Strategy #1
        diffs_idxs = {}
        for idx, val in enumerate(nums):
            diff = target - val
            if diff in diffs_idxs.keys():
                return [diffs_idxs[diff], idx]
            else:
                diffs_idxs[val] = idx

# Strategy #2
        for i in range(len(nums)):
            if target - nums[i] in nums[i + 1:]:
                return [i, nums[i + 1:].index(target - nums[i]) + 1 + i]
