from divisors import Divisors


def test_get_divisors():
    divisors_12 = Divisors(12)
    result_12: list[int] = divisors_12.get_divisors()
    assert result_12 == [2, 3, 4, 6, 12], (
        f"Expected [2, 3, 4, 6, 12], but got {result_12}"
    )

    divisors_13 = Divisors(13)
    result_13: list[int] = divisors_13.get_divisors()
    assert result_13 == [13], f"Expected [13], but got {result_13}"

    divisors_16 = Divisors(16)
    result_16: list[int] = divisors_16.get_divisors()
    assert result_16 == [2, 4, 8, 16], f"Expected [2, 4, 8, 16], but got {result_16}"

    divisors_60 = Divisors(60)
    result_60: list[int] = divisors_60.get_divisors()
    assert result_60 == [2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60], (
        f"Expected [2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60], but got {result_60}"
    )


def test_pretty_print_divisors():
    divisors_12 = Divisors(12)
    _ = divisors_12.get_divisors()
    assert divisors_12.pretty_print_factors() == "2, 3, 4, 6, 12"

    divisors_13 = Divisors(13)
    _ = divisors_13.get_divisors()
    assert divisors_13.pretty_print_factors() == "13"

    divisors_16 = Divisors(16)
    _ = divisors_16.get_divisors()
    assert divisors_16.pretty_print_factors() == "2, 4, 8, 16"

    divisors_60 = Divisors(60)
    _ = divisors_60.get_divisors()
    assert divisors_60.pretty_print_factors() == "2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60"
