#!/usr/bin/env python
# -*- coding: utf-8 -*-
############################
# Created by: Kodie Becker #
# Created on: 2021-05-26   #
############################

"""Accessory script for convert.py to parse through a folder and create a list
    of folders containing raw DVD files."""

import argparse
import csv


def parsefolder(folder):
    folder_list = [f.path for f in os.scandir(folder) if f.is_dir()]

    with open("folderlist.csv","w") as file:
        wr = csv.writer(file, dialect='excel')
        wr.writerow(folder)
        wr.writerows(folder_list)


if __name__ == '__main__':
    PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("folder", help="Folder containing individual raw movie folders")

    args = parser.parse_args()

    parsefolder(args.folder)
