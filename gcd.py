"""

Command line program to give GCD of two numbers

"""

import sys

from loguru import logger

from args import Args
from gcd import Gcd


def main() -> None:
    args: list[str] = sys.argv[1:]
    args_checker: Args = Args(
        nb_args=2, usage="Usage: python gcd.py <number1> <number2>", args=args
    )
    error: str | None = args_checker.is_valid()
    if error:
        logger.error(error)
        sys.exit(1)

    try:
        number1: int = int(args[0])
        number2: int = int(args[1])
    except ValueError:
        logger.error(
            f"Invalid number provided: ->{args[0]} /{args[1]}<-. Please provide a valid integer."
        )
        sys.exit(1)

    gcd: Gcd = Gcd(number1, number2)
    try:
        gcd_value: int = gcd.calculate_gcd()
    except ValueError as e:
        logger.error(str(e))
        sys.exit(1)

    logger.info(f"GCD of {number1} and {number2}: {gcd_value}")


if __name__ == "__main__":
    main()
