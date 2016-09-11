import urllib
import urllib.request
from bs4 import BeautifulSoup

def check_rss(url):
    openurl = urllib.request.urlopen(url)
    soup = BeautifulSoup(openurl,"html.parser")
    #xmlurl = soup.find_all('link', type='application/rss+xml')
    for link in soup.find_all('link', type='application/rss+xml'):
        print(link.get('href'), link.get('title'))
check_rss("http://chaosbude.com/")
check_rss("http://minkorrekt.")