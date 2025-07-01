import distance
from hypothesis import given, strategies as st


st_list_int_float = st.one_of(
    st.lists(st.floats(allow_infinity=False, allow_nan=False), min_size=1), st.lists(st.integers(), min_size=1)
)


@given(
    ps=st_list_int_float,
    qs=st_list_int_float,
)
def test_fuzz_euclidean(
    ps: list[int | float], qs: list[int | float]
) -> None:
    distance.euclidean(ps, qs)
