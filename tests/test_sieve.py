import sieve_of_eratosthenes
from hypothesis import given, strategies as st


# not sure how to address overflow error...
@given(n=st.integers())
def test_fuzz_sieve(n: int) -> None:
    sieve_of_eratosthenes.sieve(n)
