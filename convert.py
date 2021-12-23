#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created on: 2021-05-26
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
    ROOT = os.path.dirname(os.path.abspath(__file__))

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input",
        help="The input folder containing movie subfolders. Movie list file if -l specified.")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-l","--list",
        help="Flag to use if input is a pre-formatted list from folder parser",
        action="store_true")
    group.add_argument("-fp","--folderparser",
        help="Flag for if the folder parser script should be run in the given folder",
        action="store_true")
    parser.add_argument("-o","--output", help="Output folder")

    return (ROOT, parser.parse_args())


def convert(ROOT, args):
    if args.folderparser:
        writeFolderList(args.input, parseFolder(args.input))

    if args.list:
        with open(args.input, "r") as file:
            folder_list = csv.reader(file, dialect="excel")
            root_folder = folder_list[0]
            movie_list = folder_list[1:]
            if root_folder != args.input:
                raise InputError("CSV list should have been generated in the same folder as the input.")
    else:
        movie_list = parseFolder(args.input)

    done_file_path = ROOT + "/completed_files.csv"

    if os.path.isfile(done_file_path):
        with open(done_file_path, "r") as file:
            done_files = json.load(file)
    else:
        done_files = []

    if args.output:
        output_folder = args.output
    else:
        output_folder = ROOT

    for movie in movie_list:
        if movie in done_files:
            pass
        else:
            subprocess.run("makemkvcon -r mkv file:{0} all {1}".format(file_path, output_folder))
            done_files.append(movie)
            with open(done_file_path, "w") as file:
                json.dump(done_files, file)

    # ISO to MKV
    #     makemkvcon mkv iso:./movie.iso all .
    # Files to MKV
    #     makemkvcon mkv file:/path/to/the/VIDEO_TS/ all .


if __name__ == '__main__':
    ROOT, args = _init()
    convert(ROOT, args)
