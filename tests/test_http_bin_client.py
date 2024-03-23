from unittest.mock import Mock, patch

import pytest

from mymodule.lib.http_bin_client import HttpBinClient


@pytest.fixture
def mock_http_bin_client() -> Mock:
    return Mock(spec=HttpBinClient)


@patch("mymodule.lib.http_bin_client.HttpBinClient.get_ip")
def test_get_ip_normal(mock_http_bin_client: Mock) -> None:
    want = {"origin": "127.0.0.1"}
    mock_http_bin_client.return_value = want
    client = HttpBinClient()
    got = client.get_ip()
    assert got == want
