import pathlib

import parser
from urllib import request


class Downloader:
    def __init__(self, url: str, destination: pathlib.Path):
        self.destination = destination
        if not self.destination.exists():
            self.destination.mkdir()
        self.url = url
        self.parser = parser.Parser(self.url)

    def download(self, extension: str, verbose: bool = False):
        links = self.parser.get_links_with_extension(extension)
        for link in links:
            print(f"Downloading {link}...", end=" ")
            try:
                (filepath, response) = request.urlretrieve(link, self.destination / link[link.rfind('/') + 1:])
            except Exception as e:
                print("Failed to download!")
                print(e)
                continue
            else:
                print("Done!")
            if verbose:
                print(response)


if __name__ == '__main__':
    downloader = Downloader('https://www.cs.utexas.edu/users/EWD/index06xx.html', pathlib.Path("download_test"))
    downloader.download('pdf')
