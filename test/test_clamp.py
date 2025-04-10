# This test code was written by the `hypothesis.extra.ghostwriter` module
# and is provided under the Creative Commons Zero public domain dedication.

import clamp
import typing
from hypothesis import given, strategies as st


@given(
    value=st.one_of(st.floats(), st.integers()),
    minimum=st.one_of(st.floats(), st.integers()),
    maximum=st.one_of(st.floats(), st.integers()),
)
def test_fuzz_clamp(
    value: typing.Union[int, float],
    minimum: typing.Union[int, float],
    maximum: typing.Union[int, float],
) -> None:
    clamp.clamp(value=value, minimum=minimum, maximum=maximum)

