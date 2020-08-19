class Solution:
    def myAtoi(self, str: str) -> int:
        str = str.lstrip()
        if len(str) == 0:
            return 0
        index = 0
        if str[0] in ['+', '-']:
            index = 1
        if len(str[index:]) == 0 or not str[index].isdecimal():
            return 0
        while index < len(str):
            if not str[index].isdecimal():
                break
            index += 1
        str = int(str[:index])

        if str > 2 ** 31 - 1:
            return 2 ** 31 - 1
        elif str < -2 ** 31:
            return -2 ** 31
        else:
            return str
