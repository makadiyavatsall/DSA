class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        """
        Divides two integers without using multiplication, division, or the modulo operator.
        """
        # Define 32-bit signed integer limits
        MAX_INT = 2**31 - 1
        MIN_INT = -2**31

        # Handle the single overflow edge case as per the problem description
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT

        # 1. Determine the sign of the result.
        # A negative sign results if one number is negative, but not both.
        # The XOR operator (^) is perfect for this: (a < 0) ^ (b < 0) is true
        # only if they have different signs.
        is_negative = (dividend < 0) ^ (divisor < 0)

        # 2. Work with absolute values for easier calculation.
        a = abs(dividend)
        b = abs(divisor)

        quotient = 0
        # 3. Main loop: Subtract multiples of `b` from `a`.
        while a >= b:
            # Find the largest multiple of `b` (as a power of 2) that fits in `a`.
            # `temp_divisor` will be `b * 2^k`
            # `multiple` will be `2^k`
            temp_divisor = b
            multiple = 1
            
            # Keep doubling the `temp_divisor` and `multiple` as long as the
            # doubled `temp_divisor` still fits within `a`.
            while a >= (temp_divisor << 1):
                temp_divisor <<= 1  # Double the temporary divisor (e.g., b*2, b*4, b*8...)
                multiple <<= 1      # Double the multiple (e.g., 2, 4, 8...)
            
            # Subtract the largest multiple found from `a`.
            a -= temp_divisor
            # Add the corresponding power of 2 to the total quotient.
            quotient += multiple
            
        # 4. Apply the sign to the final quotient.
        if is_negative:
            return -quotient
        else:
            return quotient