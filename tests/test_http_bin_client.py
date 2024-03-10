from unittest.mock import Mock, patch

import pytest

from action.python.lib.http_bin_client import HttpBinClient


@pytest.fixture
def mock_http_bin_client() -> Mock:
    return Mock(spec=HttpBinClient)


@patch("action.python.lib.http_bin_client.HttpBinClient.ip")
def test_get_ip_normal(mock_http_bin_client: Mock) -> None:
    want = {"origin": "127.0.0.1"}
    mock_http_bin_client.return_value = want
    client = HttpBinClient()
    got = client.ip()
    assert got == want
