# -*- coding: utf-8 -*-
"""\
Test compat.fastnumbers module.
"""

import pytest

from natsort.compat.fastnumbers import is_supported_fastnumbers


@pytest.mark.parametrize(
    "fastnumbers_version, result",
    [
        ("0.1.2", False),
        ("0.2.0", False),
        ("0.3.0", False),
        ("0.5.0", False),
        ("0.7.3", False),
        ("1.0.0", False),
        ("2.0.0", True),
        ("2.0.1", True),
        ("2.0.2", True),
        ("2.0.5", True),
        ("2.1.0", True),
        ("2.1.1", True),
        ("2.2.0", True),
        ("3.0.0", True),
        ("3.1.0", True),
        ("4.0.0a2", True),
    ],
)
def test_is_supported_fastnumbers(fastnumbers_version: str, result: bool):
    assert is_supported_fastnumbers(fastnumbers_version) is result


def test_is_supported_fastnumbers_invalid_version():
    with pytest.raises(ValueError, match="Invalid fastnumbers version number 'hello'"):
        is_supported_fastnumbers("hello")
