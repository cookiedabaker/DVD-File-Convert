#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created on: 2021-05-26

"""Accessory script for convert.py to parse through a folder and create a list
    of folders containing raw DVD files."""

import argparse
import csv


def parseFolder(folder):
    return [f.path for f in os.scandir(folder) if f.is_dir()]

def writeFolderList(folder, folder_list):
    with open("folderlist.csv","w") as file:
        wr = csv.writer(file, dialect='excel')
        wr.writerow(folder)
        wr.writerows(folder_list)


if __name__ == '__main__':
    """Test Code"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("folder", help="Folder containing individual raw movie folders")

    args = parser.parse_args()

    writeFolderList(args.folder, parsefolder(args.folder))
