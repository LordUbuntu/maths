# This test code was written by the `hypothesis.extra.ghostwriter` module
# and is provided under the Creative Commons Zero public domain dedication.

import hamming_distance
from hypothesis import given, strategies as st

T_int_float = typing.Union[list, tuple, str]
st_int_float = st.one_of(
    st.lists(),
    st.tuples(),
    st.text(),
    st.characters()
)

@given(
    a=T_strings,
    b=T_strings,
    c=T_strings,
)
def test_associative_binary_operation_hamming_distance(
    a: hamming_distance.T, b: hamming_distance.T, c
) -> None:
    left = hamming_distance.hamming_distance(
        a=a, b=hamming_distance.hamming_distance(a=b, b=c)
    )
    right = hamming_distance.hamming_distance(
        a=hamming_distance.hamming_distance(a=a, b=b), b=c
    )
    assert left == right, (left, right)


@given(a=T_strings, b=T_strings)
def test_commutative_binary_operation_hamming_distance(
    a: hamming_distance.T, b: hamming_distance.T
) -> None:
    left = hamming_distance.hamming_distance(a=a, b=b)
    right = hamming_distance.hamming_distance(a=b, b=a)
    assert left == right, (left, right)


@given(a=T_strings)
def test_identity_binary_operation_hamming_distance(a: hamming_distance.T) -> None:
    identity = []
    assert a == hamming_distance.hamming_distance(a=a, b=identity)
    assert a == hamming_distance.hamming_distance(a=identity, b=a)

