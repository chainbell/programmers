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


s = Solution()

# Test cases
str1 = "ABCABC"
str2 = "ABC"

print(s.gcdOfStrings(str1, str2))  # Output: "ABC"

