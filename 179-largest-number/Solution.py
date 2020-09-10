from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if not nums:
            return ''
        if len(nums) == 1:
            return str(nums[0])
        max_num = max(nums)
        max_length = len(str(max_num))
        nums_copy = [int(str(num) + (max_length - len(str(num))) * max(str(num))) for num in nums]
        ans = ''
        visited = [False for _ in range(0, len(nums))]
        while False in visited:
            max_new_num = -1
            max_new_num_index = -1
            for i in range(0, len(nums_copy)):
                if not visited[i] and nums_copy[i] > max_new_num:
                    max_new_num = nums_copy[i]
                    max_new_num_index = i
            ans += str(nums[max_new_num_index])
            visited[max_new_num_index] = True
        return ans
