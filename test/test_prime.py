import pytest

from prime import MAX_PRIME, PRIME_LIST, is_prime


def test_is_prime():
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(4) == False
    assert is_prime(17) == True
    assert is_prime(25) == False


def test_is_prime_in_prime_list():
    for prime in PRIME_LIST:
        assert is_prime(prime) == True


def test_is_prime_not_in_prime_list():
    for i in range(1, MAX_PRIME + 1):
        if i not in PRIME_LIST:
            assert is_prime(i) == False


def test_prime_list():
    assert len(PRIME_LIST) == 1231


def test_max_prime():
    assert MAX_PRIME == 10007


def test_over_max_prime():
    with pytest.raises(ValueError):
        is_prime(MAX_PRIME + 1)
