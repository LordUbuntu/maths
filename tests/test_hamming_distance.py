# This test code was written by the `hypothesis.extra.ghostwriter` module
# and is provided under the Creative Commons Zero public domain dedication.


import hamming_distance
import typing
from hypothesis import given, strategies as st

T_strings = typing.Union[
    str,
    list[typing.Union[int, float, str]],
    tuple[typing.Union[int, float, str]
]
ST_strings = st.one_of(
    st.text(),
    st.lists(st.integers()),
    st.lists(st.floats(allow_nan=False, allow_infinity=False)),
    st.lists(st.text()),
    st.tuples(st.integers()),
    st.tuples(st.floats(allow_nan=False, allow_infinity=False)),
    st.tuples(st.text()),
)

# TODO: implement oracle to test behaviour itself


@given(a=ST_strings, b=ST_strings)
def test_oracle_hamming_distance(a: T_strings, b: T_strings) -> None:
    assert True  # need to find an efficient way to test with oracle...


# properties to implement are:
# - symmetry
# - triangle inequality


@given(a=ST_strings, b=ST_strings)
def test_non_negativity_hamming_distance(
    a: T_strings,
    b: T_strings
) -> None:
    assert 0 <= hamming_distance.hamming_distance(a=a, b=b)


@given(a=ST_strings, b=ST_strings)
def test_symmetry_hamming_distance(a: T_strings, b: T_strings) -> None:
    assert hamming_distance.hamming_distance(a=a, b=b) == hamming_distance.hamming_distance(a=b, b=a)


@given(a=ST_strings)
def test_identity_binary_operation_hamming_distance(a: T_strings) -> None:
    assert 0 == hamming_distance.hamming_distance(a=a, b=a)

