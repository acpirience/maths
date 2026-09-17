from gcd import Gcd


def test_gcd():
    # Test case 1: GCD of 12 and 18
    gcd_12_18 = Gcd(12, 18)
    result_12_18: int = gcd_12_18.calculate_gcd()
    assert result_12_18 == 6, f"Expected 6, but got {result_12_18}"

    gcd_8_12 = Gcd(8, 12)
    result_8_12: int = gcd_8_12.calculate_gcd()
    assert result_8_12 == 4, f"Expected 4, but got {result_8_12}"

    gcd_10000_2048 = Gcd(10000, 2048)
    result_10000_2048: int = gcd_10000_2048.calculate_gcd()
    assert result_10000_2048 == 16, f"Expected 16, but got {result_10000_2048}"

    gcd_2048_2048 = Gcd(2048, 2048)
    result_2048_2048: int = gcd_2048_2048.calculate_gcd()
    assert result_2048_2048 == 2048, f"Expected 2048, but got {result_2048_2048}"


def test_gcd_with_prime_numbers():
    # Test case 2: GCD of two prime numbers (13 and 17)
    gcd_13_17 = Gcd(13, 17)
    result_13_17: int = gcd_13_17.calculate_gcd()
    assert result_13_17 == 1, f"Expected 1, but got {result_13_17}"

    # Test case 3: GCD of a prime number and a composite number (13 and 26)
    gcd_13_26 = Gcd(13, 26)
    result_13_26: int = gcd_13_26.calculate_gcd()
    assert result_13_26 == 13, f"Expected 13, but got {result_13_26}"
