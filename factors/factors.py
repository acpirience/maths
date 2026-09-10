"""

Handles the factorisation to primes of a number

"""

from prime import MAX_PRIME, PRIME_LIST, is_prime


class Factors:
    def __init__(self, number: int) -> None:
        self.number: int = number
        self.factors: list[
            dict[int, int]
        ] = []  # key of dict is factor, value is exponent

    def factorise(self) -> list[dict[int, int]]:
        """
        Factorises the number into its prime factors.

        Returns:
            list[dict[int, int]]: A list of prime factors with their exponents.
        """
        n: int = self.number
        current_n: int = n
        prime_index: int = 0  # index of array PRIME_LIST

        if n > MAX_PRIME:
            raise ValueError(
                f"Number {n} is too large. Maximum supported prime is {MAX_PRIME}."
            )

        while True:
            prime: int = PRIME_LIST[prime_index]
            if current_n == 1:
                break

            if is_prime(current_n) or current_n < 4:
                self.factors.append({current_n: 1})
                return self.factors

            exponent: int = 0
            while current_n % prime == 0:
                exponent += 1
                current_n //= prime
            if exponent > 0:
                self.factors.append({prime: exponent})
            prime_index += 1

        return self.factors

    def pretty_print_factors(self) -> str:
        """
        Prints the prime factors in a readable format.
        """
        factor_strings: list[str] = []
        for factor_dict in self.factors:
            for factor, exponent in factor_dict.items():
                if exponent == 1:
                    factor_strings.append(f"{factor}")
                else:
                    factor_strings.append(f"{factor}^{exponent}")

        return f"{' * '.join(factor_strings)}"
