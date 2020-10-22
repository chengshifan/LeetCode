class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if not num:
            return ""
        n = len(num)
        if n == k: return "0"
        ans = ""
        nums = [int(i) for i in num]
        r_length = n - k
        while len(ans) < n - k:
            if len(nums) == r_length:
                ans += "".join([str(num) for num in nums])
                break
            min_num = min(nums[0:len(nums) - r_length + 1])
            index = nums.index(min_num)
            nums = nums[index + 1:]
            ans += str(min_num)
            r_length -= 1
        if ans.lstrip('0') == '':
            ans = '0'
        else:
            ans = ans.lstrip('0')
        return ans