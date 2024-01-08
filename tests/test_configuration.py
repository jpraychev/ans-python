import pytest


def test_raise_on_import():
    with pytest.raises(NotImplementedError):
        import ans_client.configuration