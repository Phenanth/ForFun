# -*- coding: utf-8 -*-
import os
import time
import datetime

from docs import config

"""
common.py
~~~~~~~~~~~~~~~~~~~~~~~~

This module is the initilization part of common functions

"""

# Initilize the data folder
def init_folder():

	if not os.path.exists(config.directory_path):
		os.makedirs(config.directory_path)
		print("SYSTEM: Initiated ", config.directory_path, " folder...")

# Initiation test for the relation of different modules, please ignore this
def init_test():
	testdata = "This is the test data from common. If you see this message, this shows the relations of the modules works fine."
	return testdata

# Judge if the folder path is valid.
def is_valid_path(file_path):
    
    if not os.path.exists(file_path):
        return False;
    else:
        return True;

# Read a file and return its contents
def readfile(file_path):

    with open(file_path, "r", encoding="utf-8") as f:
        texts = f.read()

    return texts

# Save a file
def savefile(data, file_path, encode):

    with open(file_path, "w", encoding=encode, errors="replace") as file_handler:
        file_handler.write(data)

# Zip a file
def zipfile(file_path, zip_file_path):

    with zipfile.ZipFile(zip_file_path, "w", compression=zipfile.ZIP_DEFLATED) as zip_handler:
        zip_handler.write(file_path, arcname=common_string.clip_file_name(file_path))

# Delete a file
def deletefile(file_path):

    os.remove(file_path)


# Using a generator to serve files, automatically delete the source file when served.
def generate(file_path, operation):

    if operation == "download":
        with open(file_path, "rb") as f:
            yield from f

    elif operation == "get":

        with open(file_path, "r", encoding="utf-8") as f:
            yield from f

    deletefile(file_path)


# Generate a string presents time
def present_time():

    date_now = datetime.datetime.now()

    year = str(date_now.year).zfill(4)
    month = str(date_now.month).zfill(2)
    day = str(date_now.day).zfill(2)
    hour = str(date_now.hour).zfill(2)
    minute = str(date_now.minute).zfill(2)
    second = str(date_now.second).zfill(2)

    return year + month + day + hour + minute + second


# Initilize a file name for series one
def file_name(filehead):

    file_name = ""

    file_name = config.directory_path + "/"

    # If the IndicatorCode is not empty, add the IndicatorCode at the end.
    if filehead != "":
        file_name = file_name + filehead + "_"

    file_name = file_name + present_time() + ".txt"

    return file_name, file_name


# Clip the file name, excluding its file path
def clip_file_name(file_path):

    return file_path[(len(config.directory_path) + 1):]
