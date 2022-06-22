class Solution:
    """this code allowed me to achieve, as of 22/06/2022:
       Runtime: 38 ms, faster than 98.22% of Python3 online submissions for Fizz Buzz.
       Memory Usage: 15 MB, less than 84.84% of Python3 online submissions for Fizz Buzz."""
    def fizzBuzz(self, n: int) -> List[str]:
        """
                :param n:
                :return:
                Given an integer n, return a string array answer (1-indexed) where:

    answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
    answer[i] == "Fizz" if i is divisible by 3.
    answer[i] == "Buzz" if i is divisible by 5.
    answer[i] == i (as a string) if none of the above conditions are true.

    Strategy:
    - calculate the remainder of the divisions by 3 and 5 and append values in amnswer list based on when they are 0
    - activate checks strategically to minimize computations
                """
        answer = []
        for i in range(1, n+1):
            mod5 = i % 5
            mod3 = i % 3
            if not mod5: # since there is a nested if, it's best to perform the one that rules out the most values first
                if not mod3:
                    answer.append("FizzBuzz")
                else:
                    answer.append("Buzz")
            else:
                if not mod3:
                    answer.append("Fizz")
                else:
                    answer.append(str(i))
        return answer
