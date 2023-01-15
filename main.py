import argparse
import pathlib

from downloader import Downloader

command_options = argparse.ArgumentParser(
    prog="Auto_downloader",
    description="Download files from a website",
    epilog="Enjoy the program! :)",
)
command_options.add_argument("url", help="The url of the website")
command_options.add_argument("extension", help="The extension of the files")
command_options.add_argument("destination", help="The destination of the files")
command_options.add_argument("-v", "--verbose", help="Print more information", action="store_true")

args = command_options.parse_args()

downloader = Downloader(args.url, pathlib.Path(args.destination))
downloader.download(args.extension, args.verbose)
print("Done!")
