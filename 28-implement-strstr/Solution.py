class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        try:
            res = haystack.index(needle)
            return res
        except Exception as err:
            return -1
