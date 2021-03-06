# -*- coding: utf-8 -*-
from docs import config
from . import common


def generate_url(fic_code, fic_index):

	return config.url_path + str(fic_code) + "/" + str(fic_index) + "/"

def data_operation(data, operation):

	success = True
	message = ""

	attachment = ""
	temp_file_name = ""

	file_path, file_name = common.file_name("fics")
	zip_file_path, zip_file_name = common.file_name("fics")

	# If the operation is download.
	if operation == "download":

		common.savefile(data, file_path, "utf-8")
		common.zipfile(file_path, zip_file_path)
		common.deletefile(file_path)

		temp_file_name = zip_file_name

	# If the operation is get.
	elif operation == "get":

		# If the save path is not valid.
		if common.is_valid_path(config.directory_path):
			common.savefile(data, file_path, "utf-8")
			temp_file_name = file_name
		else:
			success = False;
			message = "Error: Invalid Save Path."
			temp_file_name = ""

	if success:
		attachment = common.clip_file_name(temp_file_name)
	else:
		attachment = ""

	return attachment, message
