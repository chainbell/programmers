class Solution:

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        a = len(str1)
        b = len(str2)
        while b != 0:
            a, b = b, a % b

        gcd_length = a
        return str1[:gcd_length]

    def gcdOfStrings2(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ''
        for i in range(len(str1), 0, -1):
            if len(str1) % i == 0 and len(str2) % i == 0:
                return str1[:i]
s = Solution()

# Test cases
str1 = "ABCABC"
str2 = "ABC"

print(s.gcdOfStrings(str1, str2))

print(s.gcdOfStrings2(str1, str2))

