import requests
from requests import Response


class HttpBinClient(object):
    BASE_URL = "https://httpbin.org"

    def __init__(self) -> None:
        self.session = requests.Session()

    def get_ip(self) -> Response:
        return self.session.get(f"{self.BASE_URL}/ip")
