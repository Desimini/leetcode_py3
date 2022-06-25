class Solution:
    """this code allowed me to achieve, as of 25/06/2022:
    Runtime: 24 ms, faster than 98.87% of Python3 online submissions for Number of Steps to Reduce a Number to Zero.
    Memory Usage: 13.8 MB, less than 95.75% of Python3 online submissions for Number of Steps to Reduce a Number to Zero."""
    def numberOfSteps(self, num: int) -> int:
        depth = 0
        while True:
            if not num:
                return depth
            if num % 2:
                num = num - 1
            else:
                num = num / 2
            depth = depth + 1
