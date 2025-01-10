import pytest

from main import dad_who


@pytest.mark.parametrize("content, expected", [
    ("jsem programátor.", "programátor"),
    ("jsem, programátor.", ""),
    ("jsem velmi dobrý programátor.", "velmi dobrý programátor"),
    ("jsemprogramátor.", "programátor"),
    ("jsem programátor", "programátor"),
])
def test_dad_who(content, expected):
    assert dad_who(content) == expected