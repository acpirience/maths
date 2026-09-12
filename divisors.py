"""

Give the divisors of a number

"""

import sys

from loguru import logger

from args import Args
from divisors import Divisors


def main() -> None:
    args: list[str] = sys.argv[1:]
    args_checker: Args = Args(
        nb_args=1, usage="Usage: python divisors.py <number>", args=args
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

    divisors: Divisors = Divisors(number)
    _ = divisors.get_divisors()
    logger.info(f"Divisors of {number}: {divisors.pretty_print_factors()}")


if __name__ == "__main__":
    main()
