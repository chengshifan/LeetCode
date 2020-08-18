class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        sorted(candidates)
        results = []

        def find(total, candidates, result, i):
            if i >= len(candidates) or total > target:
                return
            if total == target:
                results.append(result[:])
                return
            for j in range(i, len(candidates)):
                if candidates[j] > target:
                    continue
                result.append(candidates[j])
                find(total + candidates[j], candidates, result, j)
                del result[len(result) - 1]

        find(0, candidates, [], 0)
        return results