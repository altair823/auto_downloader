import argparse
import pathlib

from downloader import Downloader


def main():
    command_options = argparse.ArgumentParser(
        prog="Auto_downloader",
        description="Download files from a website",
        epilog="Enjoy the program! :)",
    )
    command_options.add_argument("extension", help="The extension of the files")
    command_options.add_argument("destination", help="The destination of the files")
    command_options.add_argument("-urls", help="The list of urls to download from", nargs="+", required=True)
    command_options.add_argument("-v", "--verbose", help="Print more information", action="store_true")

    args = command_options.parse_args()

    for url in args.urls:
        downloader = Downloader(url, pathlib.Path(args.destination))
        downloader.download(args.extension, args.verbose)
    print("Done!")


if __name__ == '__main__':
    main()
