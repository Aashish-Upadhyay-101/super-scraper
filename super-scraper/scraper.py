from bs4 import BeautifulSoup
import urllib3 

http = urllib3.PoolManager()

r = http.request('GET', 'https://urllib3.readthedocs.io/en/stable/')

soup = BeautifulSoup(r._body, "html.parser")

print(soup.prettify())
