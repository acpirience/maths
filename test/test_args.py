from args.args import Args


def test_args_valid():
    args_checker = Args(nb_args=1, usage="Usage: python prime.py <number>", args=["5"])
    assert args_checker.is_valid() is None


def test_args_valid():
    args_checker = Args(nb_args=1, usage="Usage: python prime.py <number>", args=["1"])
    assert args_checker.is_valid() is None


def test_number_of_args_invalid():
    args_checker = Args(
        nb_args=1, usage="Usage: python prime.py <number>", args=["5", "extra_arg"]
    )
    assert args_checker.is_valid() is not None


def test_number_of_args_valid():
    args_checker = Args(nb_args=1, usage="Usage: python prime.py <number>", args=["5"])
    assert args_checker.is_valid() is None
