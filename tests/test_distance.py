import distance
from hypothesis import given, strategies as st


# how to do lists of at least 1 element?
st_int_float = st.one_of(
    st.floats(allow_infinity=False, allow_nan=False), st.integers()
)


@given(
    ps=st_list_int_float,
    qs=st_list_int_float,
)
def test_fuzz_euclidean(
    ps: list[int | float], qs: list[int | float]
) -> None:
    ditance.euclidean(ps, qs)
