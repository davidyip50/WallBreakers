class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 0
        newNum = digits[len(digits) - 1] + 1
        if(newNum >= 10):
            carry = newNum / 10
            digits[len(digits) - 1] = newNum % 10
        else:
            digits[len(digits) - 1] = newNum
            carry = 0
        for i in range(len(digits) - 2, -1, -1 ):
            newNum = digits[i] + carry
            if(newNum >= 10):
                carry = newNum / 10
                digits[i] = newNum % 10
            else:
                digits[i] = newNum
                carry = 0
        if(carry == 1):
            digits.insert(0,carry)
        return digits
