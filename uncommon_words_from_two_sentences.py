class Solution:
    """This was taken by the weelky contest 97 and solved on 26/06/2022, recorded best run:
    Runtime: 24 ms, faster than 99.01% of Python3 online submissions for Uncommon Words from Two Sentences.
    Memory Usage: 13.8 MB, less than 69.89% of Python3 online submissions for Uncommon Words from Two Sentences."""
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        """

        :param s1:
        :param s2:
        :return:
        A sentence is a string of single-space separated words where each word consists only of lowercase letters.
        A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.
        Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.

        Strategy: create a list of words by splitting the sentences and check the occurrences in same and other list,
        removing the discarded values
        """
        # initialize uncommond words list and sentences words lists
        uncommon = []
        s1_list = s1.split()
        s2_list = s2.split()

        word = s1_list.pop() # extracting the first value
        while True:
            if s1_list.count(word) == 0: # if after popping the value from the list, it's not still there (1 occurrency)
                if word not in s2_list:
                    uncommon.append(word) # add the word to uncommon if it is not in the other list
                else:
                    while word in s2_list:
                        s2_list.remove(word) # remove the word from the other list if it was there
            else:
                # remove the word from both lists if it had more than 1 occurrency in this one
                while word in s1_list:
                    s1_list.remove(word)
                while word in s2_list:
                    s2_list.remove(word)
            if not s1_list: # if the list is over
                break
            word = s1_list.pop() # next word

        if not s2_list:
            return uncommon # early return in case the second has been canceled out by previous removals

        # perform the same operations on the second list avoiding to check cases that cannot have made it to here
        word = s2_list.pop()
        while True:
            if s2_list.count(word) == 0:
                if word not in s1_list:
                    uncommon.append(word)
                else:
                    while word in s1_list:
                        s1_list.remove(word)
            else:
                while word in s2_list:
                    s2_list.remove(word)
            if not s2_list:
                break
            word = s2_list.pop()

        return uncommon