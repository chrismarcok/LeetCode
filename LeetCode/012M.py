class Solution:
    def intToRoman(self, num: int) -> str:
        res = ""
        ones, tens, hundreds, thousands = 0,0,0,0
        ones = num % 10
        num = num // 10
        tens = num % 10
        num = num // 10
        hundreds = num % 10
        num = num // 10
        thousands = num % 10

        if thousands != 0:
            res += "M" * thousands
        if hundreds != 0:
            if (hundreds == 4):
                res += "CD"
            elif (hundreds >= 5 and hundreds <= 8):
                res += "D"
                res += "C" * (hundreds - 5)
            elif (hundreds == 9):
                res += "CM"
            else:
                res += "C" * hundreds
        if tens != 0:
            if (tens == 4):
                res += "XL"
            elif (tens >= 5 and tens <= 8):
                res += "L"
                res += "X" * (tens - 5)
            elif (tens == 9):
                res += "XC"
            else:
                res += "X" * tens
        if ones != 0:
            if (ones == 4):
                res += "IV"
            elif (ones >= 5 and ones <= 8):
                res += "V"
                res += "I" * (ones - 5)
            elif (ones == 9):
                res += "IX"
            else:
                res += "I" * ones
        return res