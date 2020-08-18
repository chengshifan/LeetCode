class Solution:
    def romanToInt(self, s: str) -> int:
        numbersMap = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        specialNumbersMap = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
        num = 0
        i = 0
        while i < len(s):
            if i < len(s) - 1 and (s[i] == 'I' or s[i] == 'X' or s[i] == 'C'):
                newStr = s[i] + s[i + 1]
                if newStr in specialNumbersMap.keys():
                    num += specialNumbersMap.get(newStr)
                    i = i + 1
                else:
                    num += numbersMap.get(s[i])
            else:
                num += numbersMap.get(s[i])
            i = i + 1
        return num
