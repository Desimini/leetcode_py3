class Solution:
    """this code allowed me to achieve, as of 26/06/2022:
    Runtime: 196 ms, faster than 91.39% of Python3 online submissions for Non-decreasing Array.
    Memory Usage: 15.1 MB, less than 90.98% of Python3 online submissions for Non-decreasing Array."""

    def checkPossibility(self, nums: List[int]) -> bool:
        """
            :param nums
            :return:
            Given an array nums with n integers, your task is to check if it could become non-decreasing by modifying
            at most one element.

            Strategy: automatically approve arrays that have at most two elements, create a flag to distinguish between
            when the array is untouched vs when the element has been already manipulated. Check for every element if it
            is less or equal to the next in the list, if so, proceed with the next element, otherwise if the array has
            already been manipulated return False, otherwise flag the array as manipulated and, if the next element in
            the list is less than the previous one as well, replace it with the current one and continue"""

        second_exception = False
        if len(nums) <= 2:
            return True
        if nums[0] > nums[1]: # hard-coding the first check to be able to assume there is a previous element in the loop
            second_exception = True
            nums[0] = nums[1] # in case the first element is less than the second, the first gets replaced
        for i in range(1, len(nums) - 1): # iterating until the second to last index in order to assume a next element
            if nums[i] <= nums[i + 1]: # if non-decresing
                continue
            elif second_exception: # if decreasing for the second time
                return False
            else: # if decreasing for the first time
                second_exception = True
                if nums[i - 1] > nums[i + 1]:
                    nums[i + 1] = nums[i] # only replace the next if it is less than the previous
        return True # if it made it to here it's non-decreasing in one move