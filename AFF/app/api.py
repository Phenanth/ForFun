# -*- coding: utf-8 -*-
import os
from flask import Flask, Response, jsonify, request, make_response, redirect, url_for

from classes.downloader import common
from classes.downloader import core

from views import home

import docs

"""
__main__.api
~~~~~~~~~~~~~~~~~~~~~~~~

This module implements the AFF API.

Parameters

get_handler:
:param operation: 		The operation of retriving data. [ get | download(not finished) ]
:param ficCode:			The code of the fiction.
:param ficIndex:		The index of the specific fiction.
:param translate:		Whether the text is translated. [ trans | notrans ]
:param enattach:		The operation of retriving data. [ attach | noattach ]

get_file:
:param operation:		Same as told.
:param fileName:		The file name of saved data, not including the path of the file.

"""


api = Flask(__name__)

# Home interface
@api.route("/getParameters")
def parameter_handler():

	isValid = True
	url = "/getResult/get/"

	webParams = {}
	params = dict(request.args)

	print(params)

	if "ficCode" in params and params["ficCode"] != "":
		url = url + str(params["ficCode"]) + "/"
		del params["ficCode"]
	else:
		isValid = False
	if "ficIndex" in params and params["ficIndex"] != "": 
		url = url + str(params["ficIndex"]) + "/"
		del params["ficIndex"]
	else:
		isValid = False
	if "translation" in params:
		url = url + "trans" + "/"
		del params["translation"]
	else:
		url = url + "notrans" + "/"
	if "enattach" in params:
		url = url + "attach"
		del params["enattach"]
	else:
		url = url + "noattach"

	if len(params) > 0:
		url = url + "?"

	if "partition" in params and params["partition"] != "":
		if str(params["partition"][0]) != "":
			url = url + "partition=" + str(params["partition"]) + "&"
	if "fromLang" in params and params["fromLang"] != "":
		if str(params["fromLang"][0]) != "":
			url = url + "fromLang=" + str(params["fromLang"]) + "&"
	if "toLang" in params and params["toLang"] != "":
		if str(params["toLang"][0]) != "":
			url = url + "toLang=" + str(params["toLang"])


	print(url)

	if not isValid:
		result = {
			"success": False,
			"message": "Wrong parameters, input again please."
		}

		return make_response(jsonify(result))


	return redirect(url)


# Route api, for handling most of the calls
@api.route("/getResult/<string:operation>/<string:ficCode>/<string:ficIndex>/<string:translate>/<string:enattach>")
def get_handler(operation, ficCode, ficIndex, translate, enattach):

	result = {}

	# JSON object, for storing all of the parameters
	requestBody = {
		"operation": operation,
		"ficCode": ficCode,
		"ficIndex": ficIndex,
		"translate": translate,
		"enattach": enattach,
		"params": request.args
	}

	result = core.downloader(requestBody)

	if result["success"]:
		return redirect(url_for("get_file", fileName=result["attachment"], operation=requestBody["operation"]))

	return make_response(jsonify(result))


# Route get file, for returning a file
@api.route("/getFile/<string:operation>/<string:fileName>")
def get_file(fileName, operation):

	package_name = docs.config.directory_path + "/" + fileName

	if os.path.isfile(package_name):

		if operation == "download":
		
			file_name = common.clip_file_name(package_name)

			# print("package_name: ", package_name, ", file_name: ", file_name)

			r = api.response_class(common.generate(package_name, operation), mimetype="application/zip")
			r.headers.set("Content-Disposition", "attachment", filename=file_name)
			
			return r

		elif operation == "get":
			return Response(common.generate(package_name, operation), mimetype="text/plain")

	else:
		result = {
			"success": False,
			"status_code": 304,
			"message": "Please Check the directory_path in ./doc/config, or check if the data file is in the right directory."
		}

		return make_response(jsonify(result))


# Route test, for debugging
@api.route("/test")
def index():

	result = {
		"directory_path": docs.config.directory_path,
		"test_common": common.init_test(),
		"success": True
	}

	return make_response(jsonify(result))


# Route 404, for route error handling
@api.errorhandler(404)
def page_not_found(error):
	return make_response(jsonify({"error": "Page Not Found."}), 404)


if __name__ == "__main__":

	api.register_blueprint(home.mod)
	api.run(host="0.0.0.0", port=8210)
