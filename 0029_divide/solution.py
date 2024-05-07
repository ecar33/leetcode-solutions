class Solution:
    def divide(dividend: int, divisor: int) -> int:
        INT_MIN = -(1<<31)
        INT_MAX = (1<<31)-1

        # Handling negative inputs
        negative = (dividend < 0) != (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        
        quotient = 0
        while dividend >= divisor:
            temp_divisor = divisor
            shift_count = 0
            while temp_divisor << 1 < dividend:
                temp_divisor = temp_divisor << 1
                shift_count += 1
            dividend -= temp_divisor
            quotient += 1 << shift_count
        
        result = -quotient if negative else quotient
        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX
        return result
        

sol = Solution
dividend = -2147483648
divisor = -1
print(sol.divide(dividend, divisor))