import requests as requests
from bs4 import BeautifulSoup


class Parser:
    def __init__(self, url):
        self.url = url
        self.soup = BeautifulSoup(requests.get(self.url).text, 'lxml')
        print(self.soup)


if __name__ == '__main__':
    parser = Parser('https://www.naver.com')