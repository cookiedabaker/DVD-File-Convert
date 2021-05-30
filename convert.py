#!/usr/bin/env python
# -*- coding: utf-8 -*-
############################
# Created by: Kodie Becker #
# Created on: 2021-05-26   #
############################
"""This scipt allows for a list of folders containing raw DVD files to be
    converted using MakeMKV."""

import os
import subprocess
import argparse
import logger
import csv
import json

from folderparser import parsefolder


def _init():
    PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("folder",
        help="The input folder containing movie subfolders.")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-l","--list",
        help="Flag to use if input is a pre-formatted list from folder parser",
        action="store_true")
    group.add_argument("-fp","--folderparser",
        help="Flag for if the folder parser script should be run in the given folder",
        action="store_true")
    parser.add_argument("-o","--output", help="Output folder")

    return (PROJECT_ROOT, parser.parse_args())


def convert(PROJECT_ROOT, args):
    if args.folderparser:
        parsefolder(folder)

    done_file_path = PROJECT_ROOT + "/completed_files.csv"

    if args.l:
        with open("folderlist.csv","r") as file:
            folder_list = csv.reader(file, dialect="excel")
            root_folder = folder_list[0]
            movie_list = folder_list[1:]
            if root_folder == folder:
                pass
            else:
                raise InputError("CSV list should have been generated in the same folder as the input.")
    else:
        movie_list = folder

    if os.path.isfile(done_file_path):
        with open(done_file_path, "r") as file:
            done_files = json.load(file)
    else:
        done_files = []

    for movie in movie_list:
        if movie in done_files:
            pass
        else:
            subprocess.run("makemkvcon -r mkv file:{0} all".format(file_path))
            done_files.append(movie)
            with open(done_file_path, "w") as file:
                json.dump(done_files, file)

    # ISO to MKV
    #     makemkvcon mkv iso:./movie.iso all .
    # Files to MKV
    #     makemkvcon mkv file:/path/to/the/VIDEO_TS/ all .


if __name__ == '__main__':
    PROJECT_ROOT, args = _init()
    convert(PROJECT_ROOT, args)
