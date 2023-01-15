import requests as requests
from bs4 import BeautifulSoup


class Parser:
    def __init__(self, url):
        self.url = url
        self.soup = BeautifulSoup(requests.get(self.url).text, 'lxml')
        self.links = [link.get('href') for link in self.soup.find_all('a')]

    def get_links_with_extension(self, extension: str):
        target_links = list(filter(lambda x: x.endswith(extension.lower()), self.links))
        target_links = target_links + list(filter(lambda x: x.endswith(extension.upper()), self.links))
        # Find last "/" in self.url and remove after it
        base_link = self.url[:self.url.rfind('/') + 1]
        return list(map(lambda x: base_link + x, target_links))


if __name__ == '__main__':
    parser = Parser('https://www.cs.utexas.edu/users/EWD/index00xx.html')
    print(parser.get_links_with_extension('pdf'))
