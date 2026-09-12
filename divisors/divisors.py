"""

Give the divisors of a number

"""


class Divisors:
    def __init__(self, number: int):
        self.number: int = number
        self.divisors: list[int] = []

    def get_divisors(self):
        for current_divisor in range(2, self.number + 1):
            if self.number % current_divisor == 0:
                self.divisors.append(current_divisor)

        return self.divisors

    def pretty_print_factors(self) -> str:
        return f"{', '.join(map(str, self.divisors))}"
