class Solution:
    """this code allowed me to achieve, as of 22/06/2022:
    Runtime: 32 ms, faster than 99.71% of Python3 online submissions for Ransom Note.
    Memory Usage: 14.1 MB, less than 52.25% of Python3 online submissions for Ransom Note."""
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        :param ransomNote:
        :param magazine:
        :return:
        Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters
        from magazine and false otherwise.
        Each letter in magazine can only be used once in ransomNote.

        Strategy: check the presence every letter in ransomnote in magazine, if one is missing then return False,
        if it's present then remove it from the magazine string and go on. If everything went smoothly return True
        """
        for letter in ransomNote:
            if letter not in magazine:
                return False
            magazine = magazine.replace(letter, "", 1) #only replace one occurrence
        return True

