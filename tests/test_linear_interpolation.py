import linear_interpolation
from hypothesis import given, strategies as st


st_int_float = st.one_of(
    st.floats(allow_infinity=False, allow_nan=False), st.integers()
)


@given(
    a=st_int_float,
    b=st_int_float,
    alpha=st.floats(allow_infinity=False, allow_nan=False),
)
def test_fuzz_lerp(
    a: int | float, b: int | float, alpha: float
) -> None:
    linear_interpolation.lerp(a, b, alpha)
