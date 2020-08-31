class Solution:
    def reverseWords(self, s: str) -> str:
        no_space_s = s.lstrip().rstrip()
        if not no_space_s or no_space_s == '':
            return ''
        s_arr = no_space_s.split(" ")
        n = len(s_arr)
        res = ''
        for i in range(n - 1, -1, -1):
            if s_arr[i] != '':
                res += s_arr[i] + " "
        return res.lstrip().rstrip()
