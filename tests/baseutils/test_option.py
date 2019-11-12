"""Tests for option-related utilities."""

import typing as t

import pytest

from baseutils.option import exists


@pytest.mark.parametrize(
    "value, exp",
    ((None, False), ([], True), ({}, True), (1, True), ((1, 2, 3), True),),
)
def test_exists(value: t.Any, exp: bool) -> None:
    """It exists if it's not None."""
    assert exists(value) is exp
