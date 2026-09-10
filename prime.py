"""

command line program to check is a number is prime or not

"""

import sys

from loguru import logger

from args import Args
from prime import is_prime


def main() -> None:
    args: list[str] = sys.argv[1:]
    args_checker: Args = Args(
        nb_args=1, usage="Usage: python prime.py <number>", args=args
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

    number_is_prime: bool = is_prime(number)
    if number_is_prime:
        logger.info(f"{number} is a prime number.")
    else:
        logger.info(f"{number} is not a prime number.")


if __name__ == "__main__":
    main()
