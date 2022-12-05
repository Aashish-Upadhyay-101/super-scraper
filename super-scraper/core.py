from exceptions import RequestException
from bs4 import BeautifulSoup
from urllib3 import PoolManager
from urllib3.response import HTTPResponse
import urllib3 


class __HTTPPool:
    def __init__(self):
        self.manager = self.create_pool_manager()

    def create_pool_manager(self) -> PoolManager:
        return urllib3.PoolManager()


class HTTPRequestHandler(__HTTPPool):
    def response(self, url: str) -> HTTPResponse:
        response = self.manager.request("GET", url)
        if response.status is 404:
            raise RequestException("Invalid url")
        return response

    def get_html(self, url:str) -> bytes:
        html = self.response(url)._body
        return html
    
    def prettify_html(self, html:bytes) -> str:
        soup = BeautifulSoup(html, "html.parser")
        return soup.prettify()

        