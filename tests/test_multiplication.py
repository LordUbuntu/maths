# This test code was written by the `hypothesis.extra.ghostwriter` module
# and is provided under the Creative Commons Zero public domain dedication.

# NOTE:
# the algorithms for multiplication have inefficient time complexities
#   and so can take a long time to test.
# I wonder if there's a way to write tests that specify a limitation
#   on the time and space complexities of a given function?

import multiplication
import typing
from hypothesis import given, settings, strategies as st

st_int_float = st.one_of(st.floats(allow_infinity=False, allow_nan=False), st.integers())
T_int_float = typing.Union[int, float]


@given(a=st_int_float, b=st_int_float, c=st_int_float)
@settings(max_examples=100)
def test_associative_binary_operation_multiplication_iterative(
    a: T_int_float, b: T_int_float, c: T_int_float
) -> None:
    left = multiplication.multiplication_iterative(
        a=a,
        b=multiplication.multiplication_iterative(a=b, b=c)
    )
    left = multiplication.multiplication_iterative(
        a=multiplication.multiplication_iterative(a=b, b=c),
        b=b
    )
    assert left == right


@given(a=st_int_float, b=st_int_float)
@settings(max_examples=100)
def test_commutative_binary_operation_multiplication_iterative(
    a: T_int_float, b: T_int_float
) -> None:
    left = multiplication.multiplication_iterative(a=a, b=b)
    right = multiplication.multiplication_iterative(a=b, b=a)
    assert left == right


@given(a=st_int_float)
@settings(max_examples=100)
def test_identity_binary_operation_multiplication_iterative(
    a: T_int_float
) -> None:
    identity = 1
    assert a == multiplication.multiplication_iterative(a=a, b=identity)
    assert a == multiplication.multiplication_iterative(a=identity, b=a)


@given(a=st_int_float)
@settings(max_examples=100)
def test_idempotence_binary_operation_multiplication_iterative(
    a: T_int_float
) -> None:
    idempotent = 0
    assert 0 == multiplication.multiplication_iterative(a=a, b=0)
    assert 0 == multiplication.multiplication_iterative(a=0, b=a)


@given(
    a=st_int_float,
    b=st_int_float,
    c=st_int_float,
)
@settings(max_examples=100)
def test_associative_binary_operation_multiplication_recursive(
    a: T_int_float, b: T_int_float, c: T_int_float
) -> None:
    left = multiplication.multiplication_recursive(a=a, b=multiplication.multiplication_recursive(a=b, b=c))
    right = multiplication.multiplication_recursive(a=multiplication.multiplication_recursive(a=a, b=b), b=c)
    assert left == right


@given(a=st_int_float, b=st_int_float)
@settings(max_examples=100)
def test_commutative_binary_operation_multiplication_recursive(
    a: T_int_float, b: T_int_float
) -> None:
    left = multiplication.multiplication_recursive(a=a, b=b)
    right = multiplication.multiplication_recursive(a=b, b=a)
    assert left == right


@given(a=st_int_float)
@settings(max_examples=100)
def test_identity_binary_operation_multiplication_recursive(
    a: T_int_float
) -> None:
    identity = 1
    assert a == multiplication.multiplication_recursive(a=a, b=identity)
    assert a == multiplication.multiplication_recursive(a=identity, b=a)


@given(a=st_int_float)
@settings(max_examples=100)
def test_idempotence_binary_operation_multiplication_recursive(
    a: T_int_float
) -> None
    idempotent = 0
    assert 0 == multiplication.multiplication_recursive(a=a, b=0)
    assert 0 == multiplication.multiplication_recursive(a=0, b=a)


