class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        results = []

        def helper(first=1, result=[]):
            if len(result) == k:
                results.append(result[:])
                return
            else:
                for num in range(first, n + 1):
                    result.append(num)
                    helper(num + 1, result)
                    result.pop()

        helper()
        return results