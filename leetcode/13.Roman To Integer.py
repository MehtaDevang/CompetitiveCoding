class Solution:
    def romanToInt(self, s: str) -> int:
        symbol_mapper = {
            "I" : 1,
            "V": 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M": 1000
        }
        
        subtraction_mapper = {
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900
        }

        value = 0

        n = len(s)
        index = 0
        while index < n:
            symbol = s[index]
            main_val = symbol_mapper[symbol]
            if index + 1 < n and symbol + s[index+1] in subtraction_mapper:
                main_val = subtraction_mapper[symbol + s[index+1]]
                index+=1                
            value += main_val
            index+=1

        return value
        