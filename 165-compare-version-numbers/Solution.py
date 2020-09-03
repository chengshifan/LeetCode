class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return '0'
        if denominator == 1:
            return str(numerator)
        flag = True if numerator * denominator > 0 else False
        numerator_abs = abs(numerator)
        denominator_abs = abs(denominator)
        pre_mod_num = -1
        res = ''
        mod_nums = []
        while True:
            num = numerator_abs // denominator_abs
            res += str(num)
            mod_num = numerator_abs - num * denominator_abs
            if mod_num == 0:
                break
            if '.' not in res:
                res += '.'
            numerator_abs = mod_num * 10
            if pre_mod_num == -1:
                pre_mod_num = mod_num
                mod_nums.append(mod_num)
            else:
                if mod_num not in mod_nums:
                    pre_mod_num = mod_num
                    mod_nums.append(mod_num)
                    continue
                else:
                    begin = mod_nums.index(mod_num)
                    res = res.split(".")[0] + "." + res.split(".")[-1][0:begin] + "(" + res.split(".")[-1][begin:] + ")"
                    break
        return res if flag else '-' + res
