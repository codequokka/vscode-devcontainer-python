import requests
from requests import Response


class HttpBinClient(object):
    base = "https://httpbin.org"

    def __init__(self) -> None:
        self.session = requests.Session()

    def ip(self) -> Response:
        return self.session.get(f"{self.base}/ip")
