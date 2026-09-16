"""

Give the prime factorisation of a given number

"""

import sys

from loguru import logger

from args import Args
from factors import Factors


def main() -> None:
    args: list[str] = sys.argv[1:]
    args_checker: Args = Args(
        nb_args=1, usage="Usage: python prime_factor.py <number>", args=args
    )
    error: str | None = args_checker.is_valid()
    if error:
        logger.error(error)
        sys.exit(1)

    try:
        number: int = int(args[0])
    except ValueError:
        logger.error(
            f"Invalid number provided: ->{args[0]}<-. Please provide a valid integer."
        )
        sys.exit(1)

    factors: Factors = Factors(number)
    try:
        _ = factors.get_factors()
    except ValueError as e:
        logger.error(str(e))
        sys.exit(1)

    logger.info(f"Prime factorisation of {number}: {factors.pretty_print_factors()}")


if __name__ == "__main__":
    main()
