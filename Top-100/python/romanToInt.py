class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        result = 0
        i = 0
        while i < len(s):
            current = roman_to_int[s[i]]
            if i + 1 < len(s) and roman_to_int[s[i + 1]] > current:
                result += roman_to_int[s[i + 1]] - current
                i += 2
            else:
                result += current
                i += 1

        return result