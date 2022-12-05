
class BaseScrapyException(Exception):
    """Base exception used by this module."""


class HTTPException(BaseScrapyException):
    """HTTPException used by this module to handle exception related to http."""


class RequestException(HTTPException):
    """RequestException used by this module."""

    def __init__(self, message: str) -> None: 
        self.message = message 
        super().__init__(self.message)


