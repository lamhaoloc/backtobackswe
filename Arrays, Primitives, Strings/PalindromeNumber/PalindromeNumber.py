'''
  Palindrome Number - LeetCode: https://leetcode.com/problems/palindrome-number/
  This code passes all Leetcode test cases as of Dec. 23 2019
'''

import math


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # If x <0 this number can't be palindrome
        if x <= 0:
            return x == 0

        len_number = math.floor(math.log10(x)) + 1
        msd_mask = math.pow(10, len_number - 1)
        # Every time we check the 1 digit with the last digit
        for i in range(int(len_number) // 2):
            if x // msd_mask != x % 10:
                return False
            x %= msd_mask  # Remove most significant digit of x
            x //= 10  # Remove last significant digit of x
            msd_mask //= 100
        return True