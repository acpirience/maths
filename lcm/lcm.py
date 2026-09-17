"""

Calculate the least common multiple (LCM) of two integers using their prime factorization.


"""

from factors.factors import Factors


class Lcm:
    def __init__(self, a: int, b: int):
        self.a: int = a
        self.b: int = b

        self.factors_a = Factors(self.a)
        self.factors_b = Factors(self.b)

    def calculate_lcm(self) -> int:
        """
        Calculate the LCM of two integers using their prime factorization.

        Returns:
            int: The LCM of the two integers.
        """
        a_factors: list[dict[int, int]] = self.factors_a.get_factors()
        b_factors: list[dict[int, int]] = self.factors_b.get_factors()

        # Create a dictionary to store the maximum exponents of all factors
        all_factors: dict[int, int] = {}

        # Find all factors and their maximum exponents
        for factor_dict_a in a_factors:
            for factor_a, exponent_a in factor_dict_a.items():
                if factor_a in all_factors:
                    all_factors[factor_a] = max(all_factors[factor_a], exponent_a)
                else:
                    all_factors[factor_a] = exponent_a

        for factor_dict_b in b_factors:
            for factor_b, exponent_b in factor_dict_b.items():
                if factor_b in all_factors:
                    all_factors[factor_b] = max(all_factors[factor_b], exponent_b)
                else:
                    all_factors[factor_b] = exponent_b

        # Calculate the LCM by multiplying the factors raised to their maximum exponents
        lcm_value: int = 1
        for factor, exponent in all_factors.items():
            lcm_value *= factor**exponent

        return lcm_value
