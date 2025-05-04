# This test code was written by the `hypothesis.extra.ghostwriter` module
# and is provided under the Creative Commons Zero public domain dedication.

import clamp
import typing
from hypothesis import given, strategies as st


st_int_float = st.one_of(st.floats(allow_infinity=False, allow_nan=False), st.integers())
T_int_float = typing.Union[int, float]  # backwards compatable `int | float`


@given(
    value=st_int_float,
    minimum=st_int_float,
    maximum=st_int_float,
)
def test_fuzz_clamp(
        value: T_int_float,
        minimum: T_int_float,
        maximum: T_int_float
) -> None:
    clamp.clamp(value=value, minimum=minimum, maximum=maximum)
