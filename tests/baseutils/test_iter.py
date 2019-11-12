"""Test iteration utilities."""

import typing as t

import pytest

from baseutils.iter import first, for_each, take


@pytest.mark.parametrize(
    "iterable, exp",
    ((range(0, 3), [0, 1, 2]), ((1, 2, 3), [1, 2, 3]), ((), []),),
)
def test_for_each(iterable: t.Iterable[int], exp: t.List[int]) -> None:
    """It consumes an iterator, applying a function as it goes."""
    mutable_target = []

    def side_effect_fn(item: int) -> None:
        mutable_target.append(item)

    for_each(side_effect_fn, iterable)

    assert mutable_target == exp


@pytest.mark.parametrize(
    "iterable, n, exp",
    (
        (range(5), 2, [0, 1]),
        ([1, 2, 3], 1, [1]),
        ([1, 2, 3], 10, [1, 2, 3]),
        ([], 5, []),
        ((1, 2), 0, []),
        ("foobar", 3, ["f", "o", "o"]),
    ),
)
def test_take(iterable: t.Iterable[t.Any], n: int, exp: t.List[t.Any]) -> None:
    """It takes items out of an iterator if available."""
    assert list(take(n, iterable)) == exp


@pytest.mark.parametrize(
    "iterable, exp",
    (
        ([], None),
        ((), None),
        (iter(()), None),
        (range(1000), 0),
        ((1, 2, 3), 1),
    ),
)
def test_first(iterable: t.Iterable[t.Any], exp: t.Any) -> None:
    """It takes the first item or returns None otherwise."""
    assert first(iterable) == exp
