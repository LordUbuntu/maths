# This test code was written by the `hypothesis.extra.ghostwriter` module
# and is provided under the Creative Commons Zero public domain dedication.

import multiplication
import typing
from hypothesis import given, strategies as st

multiplication_iterative_operands = st.one_of(st.floats(), st.integers())


@given(
    a=multiplication_iterative_operands,
    b=multiplication_iterative_operands,
    c=multiplication_iterative_operands,
)
def test_associative_binary_operation_multiplication_iterative(
    a: typing.Union[int, float], b: typing.Union[int, float], c
) -> None:
    left = multiplication.multiplication_iterative(
        a=a, b=multiplication.multiplication_iterative(a=b, b=c)
    )
    right = multiplication.multiplication_iterative(
        a=multiplication.multiplication_iterative(a=a, b=b), b=c
    )
    assert left == right, (left, right)


@given(a=multiplication_iterative_operands, b=multiplication_iterative_operands)
def test_commutative_binary_operation_multiplication_iterative(
    a: typing.Union[int, float], b: typing.Union[int, float]
) -> None:
    left = multiplication.multiplication_iterative(a=a, b=b)
    right = multiplication.multiplication_iterative(a=b, b=a)
    assert left == right, (left, right)


@given(a=multiplication_iterative_operands)
def test_identity_binary_operation_multiplication_iterative(
    a: typing.Union[int, float]
) -> None:
    # I'm sure this isn't correct...
    # Multiplying by 0 should always yield 0.
    # Multiplying by 1 should always yield a.
    identity = 0.0
    assert a == multiplication.multiplication_iterative(a=a, b=identity)
    assert a == multiplication.multiplication_iterative(a=identity, b=a)


multiplication_recursive_operands = st.one_of(st.floats(), st.integers())


@given(
    a=multiplication_recursive_operands,
    b=multiplication_recursive_operands,
    c=multiplication_recursive_operands,
)
def test_associative_binary_operation_multiplication_recursive(
    a: typing.Union[int, float], b: typing.Union[int, float], c
) -> None:
    left = multiplication.multiplication_recursive(
        a=a, b=multiplication.multiplication_recursive(a=b, b=c)
    )
    right = multiplication.multiplication_recursive(
        a=multiplication.multiplication_recursive(a=a, b=b), b=c
    )
    assert left == right, (left, right)


@given(a=multiplication_recursive_operands, b=multiplication_recursive_operands)
def test_commutative_binary_operation_multiplication_recursive(
    a: typing.Union[int, float], b: typing.Union[int, float]
) -> None:
    left = multiplication.multiplication_recursive(a=a, b=b)
    right = multiplication.multiplication_recursive(a=b, b=a)
    assert left == right, (left, right)


@given(a=multiplication_recursive_operands)
def test_identity_binary_operation_multiplication_recursive(
    a: typing.Union[int, float]
) -> None:
    identity = 0.0
    assert a == multiplication.multiplication_recursive(a=a, b=identity)
    assert a == multiplication.multiplication_recursive(a=identity, b=a)

