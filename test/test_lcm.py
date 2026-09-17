from lcm import Lcm


def test_lcm():
    # Test case 1: LCM of 12 and 18
    lcm_12_18 = Lcm(12, 18)
    result_12_18: int = lcm_12_18.calculate_lcm()
    assert result_12_18 == 36, f"Expected 36, but got {result_12_18}"

    lcm_8_12 = Lcm(8, 12)
    result_8_12: int = lcm_8_12.calculate_lcm()
    assert result_8_12 == 24, f"Expected 24, but got {result_8_12}"

    lcm_10000_2048 = Lcm(10000, 2048)
    result_10000_2048: int = lcm_10000_2048.calculate_lcm()
    assert result_10000_2048 == 1280000, f"Expected 32, but got {result_10000_2048}"


def test_lcm_with_prime_numbers():
    lcm_13_17 = Lcm(13, 17)
    result_13_17: int = lcm_13_17.calculate_lcm()
    assert result_13_17 == 221, f"Expected 221, but got {result_13_17}"

    lcm_13_26 = Lcm(13, 26)
    result_13_26: int = lcm_13_26.calculate_lcm()
    assert result_13_26 == 26, f"Expected 26, but got {result_13_26}"
