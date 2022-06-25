class Solution:
    """this code allowed me to achieve, as of 25/06/2022:
    Runtime: 61 ms, faster than 82.42% of Python3 online submissions for Richest Customer Wealth.
    Memory Usage: 13.9 MB, less than 73.19% of Python3 online submissions for Richest Customer Wealth."""
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        """
                :param accounts
                :return: Given the accounts grid that represents the money each customer (row) has in every bank (column)
                return the total wealth of the ruchest customer


                Strategy: store the wealth of the first customer as the sum of its row and iterate over other rows
                comparing at every step, returning the final value
                """
        max_wealth = sum(accounts[0])
        for i in range(1, len(accounts)):
            customer_wealth = sum(accounts[i])
            if customer_wealth > max_wealth:
                max_wealth = customer_wealth
        return max_wealth
