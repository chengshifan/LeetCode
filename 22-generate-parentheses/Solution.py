class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []

        def helper(cur, n, left, right, result):
            if right == n:
                result.append(cur)
                return
            if left < n:
                helper(cur + "(", n, left + 1, right, result)
            if right < left:
                helper(cur + ")", n, left, right + 1, result)

        helper("", n, 0, 0, result)
        return result
