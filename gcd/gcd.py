"""

Calculate the greatest common divisor (GCD) of two integers using the Euclidean algorithm.


"""

from factors.factors import Factors


class Gcd:
    def __init__(self, a: int, b: int):
        self.a: int = a
        self.b: int = b

        self.factors_a = Factors(self.a)
        self.factors_b = Factors(self.b)

    def calculate_gcd(self) -> int:
        """
        Calculate the GCD of two integers using the Euclidean algorithm.

        Returns:
            int: The GCD of the two integers.
        """
        a_factors: list[dict[int, int]] = self.factors_a.get_factors()
        b_factors: list[dict[int, int]] = self.factors_b.get_factors()

        # Create a dictionary to store the minimum exponents of common factors
        common_factors: dict[int, int] = {}

        # Find common factors and their minimum exponents
        for factor_dict_a in a_factors:
            for factor_a, exponent_a in factor_dict_a.items():
                for factor_dict_b in b_factors:
                    if factor_a in factor_dict_b:
                        exponent_b: int = factor_dict_b[factor_a]
                        common_exponent: int = min(exponent_a, exponent_b)
                        common_factors[factor_a] = common_exponent
        # Calculate the GCD by multiplying the common factors raised to their minimum exponents
        gcd_value: int = 1
        for factor, exponent in common_factors.items():
            gcd_value *= factor**exponent

        return gcd_value
