import pytest

from factors import Factors
from prime import MAX_PRIME


def test_factorisation():
    # Test case 1: Factorisation of 12
    factors_3 = Factors(3)
    result_3: list[dict[int, int]] = factors_3.factorise()
    assert result_3 == [{3: 1}], f"Expected [{3: 1}], but got {result_3}"

    factors_8 = Factors(8)
    result_8: list[dict[int, int]] = factors_8.factorise()
    assert result_8 == [{2: 3}], f"Expected [{2: 3}], but got {result_8}"

    factors_12 = Factors(12)
    result_12 = factors_12.factorise()
    assert result_12 == [{2: 2}, {3: 1}], (
        f"Expected [{2: 2}, {3: 1}], but got {result_12}"
    )

    factors_13 = Factors(13)
    result_13: list[dict[int, int]] = factors_13.factorise()
    assert result_13 == [{13: 1}], f"Expected [{13: 1}], but got {result_13}"

    factors_40 = Factors(40)
    result_40: list[dict[int, int]] = factors_40.factorise()
    assert result_40 == [{2: 3}, {5: 1}], (
        f"Expected [{2: 3}, {5: 1}], but got {result_40}"
    )

    factors_60 = Factors(60)
    result_60 = factors_60.factorise()
    assert result_60 == [{2: 2}, {3: 1}, {5: 1}], (
        f"Expected [{2: 2}, {3: 1}, {5: 1}], but got {result_60}"
    )

    factors_1001 = Factors(1001)
    result_1001: list[dict[int, int]] = factors_1001.factorise()
    assert result_1001 == [{7: 1}, {11: 1}, {13: 1}], (
        f"Expected [{7: 1}, {11: 1}, {13: 1}], but got {result_1001}"
    )


def test_factorisation_of_a_too_large_number():
    # Test case 5: Factorisation of a large number (MAX_PRIME + 1)
    with pytest.raises(ValueError):
        _ = Factors(MAX_PRIME + 1).factorise()


def test_pretty_print_factors():
    # Test case 6: Pretty print of factors
    factors_12 = Factors(12)
    result_12: list[dict[int, int]] = factors_12.factorise()
    pretty_result_12 = factors_12.pretty_print_factors()
    assert pretty_result_12 == "2^2 * 3", (
        f"Expected '2^2 * 3', but got {pretty_result_12}"
    )

    factors_512 = Factors(512)
    result_512 = factors_512.factorise()
    pretty_result_512 = factors_512.pretty_print_factors()
    assert pretty_result_512 == "2^9", f"Expected '2^9', but got {pretty_result_512}"

    factors_1001 = Factors(1001)
    result_1001: list[dict[int, int]] = factors_1001.factorise()
    pretty_result_1001 = factors_1001.pretty_print_factors()
    assert pretty_result_1001 == "7 * 11 * 13", (
        f"Expected '7 * 11 * 13', but got {pretty_result_1001}"
    )
