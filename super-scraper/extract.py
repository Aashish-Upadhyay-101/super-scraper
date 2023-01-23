from scraper import HTTPRequestResponseHandler
from bs4 import BeautifulSoup

handler = HTTPRequestResponseHandler("https://stackoverflow.com/questions/12117087/python-hide-methods-with")

def extract_meta():
    """
    The function to extract meta tag.

    Returns:   
        meta_list (list) : List of Meta tags contents
    """

    handler.response()
    html = handler.get_html()
    soup = BeautifulSoup(html, 'html.parser')
    
    meta_list = [] 
    for tag in soup.find_all("meta"):
        one_list = [] 
        one_list.append(tag.get("name", ""))
        one_list.append(tag.get("content", ""))
        meta_list.append(one_list)

    return meta_list

def extract_images_url(): 
    """
    The function to extract all image of a webpage

    Returns:
        image_urls (list) : List of image urls
    """

    image_urls = []
    return image_urls





