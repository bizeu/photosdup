#!/usr/bin/env python3.9
# coding=utf-8
"""
Photosdup Photosdup Module
"""

from multiprocessing.spawn import freeze_support
from pathlib import Path
from photosdup import DuplicateFinder
from rich import print
from rich.traceback import install

DIR = False
LIBRARY = "~/Pictures/Photo Library.photoslibrary"
DIRECTORY = "~/Photos/Output/MediaAfterSep2016"
TEST = "~/Pictures/test.photoslibrary"

PREFIX = "photosdup"
RADIUSES = [400, 1700]  # Default: [400, 1000]
THUMBS = True
XDIMS = [10, 50]  # [ Default: [10, 50]
YDIMS = [10, 50]  # [ Default: [10, 50]

# GOOD: [1000, 1000] Thumbs: True/False (Doesn't the low-res picture)
# GOOD: [400, 1000] Thumbs: True/False (Doesn't the low-res picture)
# BEST: [400, 1000] Thumbs: True/False
# BEST: [300, 1200] Thumbs: True (Better: high-res to low-res at least 1 out of 3)
# BEST: [400, 1500] Thumbs: True (Even better: high-res to low-res at least 2 out of 3)
# BEST: [400, 1700] Thumbs: True (The best: high-res to low-res 3 out of 3)


def trace():
    install(show_locals=True)


if __name__ == "__main__":

    directory = str(Path(DIRECTORY if DIR else TEST).expanduser())

    freeze_support()
    trace()
    print("[bold blue]Starting[/bold blue]: [bold yellow]directory[/bold yellow]")
    print("")

    df = DuplicateFinder(directory)

    print(df.scan(dimensions=tuple(zip(XDIMS, YDIMS)),
                  prefix=None if DIR else "photosdup",
                  radiuses=RADIUSES,
                  thumbs=THUMBS))
