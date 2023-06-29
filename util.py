import pathlib
import json
import pandas as pd

from exceptions import *

"""
Untility functions:
* Saving {marker, content, parquets}
* Reading {marker, content, parquets}
* Paths
"""

def save_marker(path, content):
    if not pathlib.Path(path).exists():
        pathlib.Path(path).parents[0].mkdir(parents=True, exist_ok=True)
    save_content(
        path=path,
        content=content
    )
    print("Marker is written to {}".format(path))


def read_marker(path):
    if not pathlib.Path(path).exists():
        raise PaginatedParseMarkerNotFound(marker_fpath=path)
    return json.loads(read_content(path))


def save_parquet(path, df: pd.DataFrame):
    if not pathlib.Path(path).exists():
        pathlib.Path(path).parents[0].mkdir(parents=True, exist_ok=True)
    df.to_parquet(path=path, engine='pyarrow')
    print("Parquet is written to {}".format(path))


def save_content(path, content):
    if not pathlib.Path(path).exists():
        pathlib.Path(path).parents[0].mkdir(parents=True, exist_ok=True)
    print("Saving: {}...".format(path))
    with open(path, "w") as file:
        file.write(content)
    print("Content is saved to {}".format(path))


def read_content(path):
    content = None
    print("Reading: {}...".format(path))
    with open(path, "r") as file:
        content = file.read()
    print(len(content))
    return content