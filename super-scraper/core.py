from exceptions import RequestException
from bs4 import BeautifulSoup
from urllib3 import PoolManager
from urllib3.response import HTTPResponse
import urllib3 


class __HTTPPool:
    """Private class to create PoolManager instance."""

    def __init__(self):
        self.manager = self.create_pool_manager()

    def create_pool_manager(self) -> PoolManager:
        return urllib3.PoolManager()


class HTTPRequestResponseHandler(__HTTPPool):
    """This class is responsible for request and response handling"""

    def response(self, url: str) -> HTTPResponse:
        """
        The function to get the response of given url.

        Parameters:
            url (str) : The url string to send the request to.

        Returns: 
            HTTPResponse: A response object of the given url endpoint.
        """
        response = self.manager.request("GET", url)
        if response.status is 404:
            raise RequestException("Invalid url")
        return response

    def get_html(self, url:str) -> bytes:
        """
        The function to retrieve HTML document of the given url.

        Parameters:
            url (str) : The url string to send the request to.
        
        Returns: 
            html (bytes) : bytes object form of html document.
        """

        html = self.response(url)._body
        return html
    
    def prettify_html(self, html:bytes) -> str:
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

