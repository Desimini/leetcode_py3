class Solution:
    """this code allowed me to achieve, as of 22/06/2022:
          Runtime: 112 ms, faster than 94.45% of Python3 online submissions for The K Weakest Rows in a Matrix.
          Memory Usage: 14.1 MB, less than 98.73% of Python3 online submissions for The K Weakest Rows in a Matrix."""
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        """

        :param mat:
        :param k:
        :return:
        You are given an m x n binary matrix mat of 1's (representing soldiers) and 0's (representing civilians).
        The soldiers are positioned in front of the civilians. That is, all the 1's will appear to the left of all the 0's in each row.
        A row i is weaker than a row j if one of the following is true:
        The number of soldiers in row i is less than the number of soldiers in row j.
        Both rows have the same number of soldiers and i < j.
        Return the indices of the k weakest rows in the matrix ordered from weakest to strongest.

        Strategy: sort the matrix with a key function summing all the elements of a row plus adding a small residual,
                    which is always less than one, to differentiate between same
        """
        m = len(mat)
        sorted_mat = sorted(mat, key=lambda row: sum(row))
        k_weakest = []
        i = 0
        old_row = None
        for i in range(k):
            ith_row = sorted_mat[i]
            if ith_row == old_row:
                continue
            for idx in range(m):
                if mat[idx] == ith_row:
                    k_weakest.append(idx)
            old_row = ith_row
            if len(k_weakest) == k:
                break
        return k_weakest[:k]

