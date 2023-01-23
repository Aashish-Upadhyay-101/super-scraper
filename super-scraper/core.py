from exceptions import RequestException
from bs4 import BeautifulSoup
from urllib3 import PoolManager
from urllib3.response import HTTPResponse


class __HTTPPool:
    """Private class to create PoolManager instance."""

    def __init__(self):
        self.manager = self.__create_pool_manager()

    def __create_pool_manager(self) -> PoolManager:
        return PoolManager()


class HTTPRequestResponseHandler(__HTTPPool):
    """This class is responsible for request and response handling"""

    def __init__(self, url: str) -> None:
        """
        Constructor of HTTPRequestResponseHandler class

        Parameters: 
            url (str) : The url string to send the request to
        """
        self.url = url
        super().__init__()

    def response(self) -> HTTPResponse:
        """
        The function to get the response of given url.

        Returns: 
            HTTPResponse: A response object of the given url endpoint.
        """
        response = self.manager.request("GET", self.url)
        if response.status == 404:
            raise RequestException("Invalid url")
        return response

    def get_html(self) -> bytes:
        """
        The function to retrieve HTML document of the given url.

        Returns: 
            html (bytes) : bytes object form of html document.
        """

        html = self.response()._body
        return html
    
    def prettify_html(self, html: bytes) -> str:
        """
        The function to Prettify the html document.

        Parameters:
            html (bytes) : bytes object form of html document.

        Returns: 
            prettified_html (str) : human readable and prettified html document.
        """

        soup = BeautifulSoup(html, "html.parser")

        prettified_html = soup.prettify();
        return prettified_html


