from typing import List


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(c.lower() for c in s if c.isalnum())
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return False
            else:
                left += 1
                right -= 1
        return True



sol = Solution()

# Example 1:
print(sol.isPalindrome("A man, a plan, a canal: Panama"))

# Example 2:
print(sol.isPalindrome("race a car"))

print(sol.isPalindrome(" "))