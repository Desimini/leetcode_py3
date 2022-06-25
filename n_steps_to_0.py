class Solution:
    """this code allowed me to achieve, as of 25/06/2022:
    Runtime: 24 ms, faster than 98.87% of Python3 online submissions for Number of Steps to Reduce a Number to Zero.
    Memory Usage: 13.8 MB, less than 95.75% of Python3 online submissions for Number of Steps to Reduce a Number to Zero."""
    def numberOfSteps(self, num: int) -> int:
        """
                :param num
                :return:
                Given an integer num, return the number of steps to reduce it to zero.
                In one step, if the current number is even, you have to divide it by 2, otherwise, you have to subtract
                1 from it.

                Strategy: check the remainder of the division by two to decide the operation to apply and increase the
                depth parameter to keep track of the amount of steps
                """
        depth = 0
        while True:
            if not num:
                return depth
            if num % 2:
                num = num - 1
            else:
                num = num / 2
            depth = depth + 1
