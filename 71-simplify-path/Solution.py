class Solution:
    def simplifyPath(self, path: str) -> str:
        res = '/'
        if not path:
            return res
        dirs = path.split("/")
        stack = []
        for dir in dirs:
            if dir == '' or dir == '.':
                continue
            elif dir == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(dir)
        for data in stack:
            res += data + '/'
        return res[0:-1] if len(res) > 1 else '/'
