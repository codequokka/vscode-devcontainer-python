from unittest.mock import Mock, patch

import pytest
import requests

from mymodule.lib.http_bin_client import HttpBinClient


@pytest.fixture
def mock_http_bin_client() -> Mock:
    return Mock(spec=HttpBinClient)


@patch("mymodule.lib.http_bin_client.HttpBinClient.get_ip")
def test_get_ip_success(mock_http_bin_client: Mock) -> None:
    want = {"origin": "127.0.0.1"}
    mock_http_bin_client.return_value = want

    client = HttpBinClient()
    got = client.get_ip()

    assert got == want


@patch("mymodule.lib.http_bin_client.HttpBinClient.get_ip")
def test_get_ip_fail(mock_http_bin_client: Mock) -> None:
    mock_http_bin_client.side_effect = Exception("Request failed")

    client = HttpBinClient()
    with pytest.raises(Exception) as exc_info:
        client.get_ip()

    assert str(exc_info.value) == "Request failed"


# @patch("mymodule.lib.http_bin_client.HttpBinClient.get_ip")
# def test_get_ip_failure_404(mock_http_bin_client: Mock) -> None:
#     # モックが404応答を返すように設定
#     mock_http_bin_client.return_value = {"status_code": 404, "error": "Not Found"}

#     client = HttpBinClient()
#     with pytest.raises(requests.exceptions.RequestException) as exc_info:
#         client.get_ip()

#     # 404応答が返されることを確認
#     assert str(exc_info.value) == "HTTP request returned 404: Not Found"
