# This test code was written by the `hypothesis.extra.ghostwriter` module
# and is provided under the Creative Commons Zero public domain dedication.

import hamming_distance
from hypothesis import given, strategies as st

hamming_distance_operands = st.from_type(~T)


@given(
    a=hamming_distance_operands,
    b=hamming_distance_operands,
    c=hamming_distance_operands,
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


@given(a=hamming_distance_operands, b=hamming_distance_operands)
def test_commutative_binary_operation_hamming_distance(
    a: hamming_distance.T, b: hamming_distance.T
) -> None:
    left = hamming_distance.hamming_distance(a=a, b=b)
    right = hamming_distance.hamming_distance(a=b, b=a)
    assert left == right, (left, right)


@given(a=hamming_distance_operands)
def test_identity_binary_operation_hamming_distance(a: hamming_distance.T) -> None:
    identity = []
    assert a == hamming_distance.hamming_distance(a=a, b=identity)
    assert a == hamming_distance.hamming_distance(a=identity, b=a)

