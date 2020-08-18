class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        meta = {'(': ')', '[': ']', '{': '}'}
        list = []
        for c in s:
            if c == '(' or c == '[' or c == '{':
                list.append(c)
            else:
                try:
                    cur = list.pop()
                except Exception as e:
                    return False

                if meta[cur] != c:
                    return False
        return not list
