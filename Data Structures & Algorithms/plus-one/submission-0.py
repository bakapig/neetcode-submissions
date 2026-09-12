class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        digs = int(''.join([str(digit) for digit in digits])) + 1

        return [str(dig) for dig in str(digs)]
        