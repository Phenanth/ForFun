# -*- coding: utf-8 -*-
import requests
import random
import hashlib

from docs import config
from . import common

def init(text, appid, salt, secretKey):

	sign = appid + text + str(salt) + secretKey
	m1 = hashlib.md5()
	m1.update(sign.encode("utf-8"))
	sign = m1.hexdigest()

	return sign

def generateParams(text, fromLang, toLang, appid, salt, sign):

	params = {}

	params.update({"q": text})
	params.update({"from": fromLang})
	params.update({"to": toLang})
	params.update({"appid": appid})
	params.update({"salt": salt})
	params.update({"sign": sign})

	return params

def getResponse(url, params):

	return requests.get(url, params).json()["trans_result"]

def generateResult(results, enattach):

	fics = ""

	for result in results:
		# 双语开关为开
		if enattach:
			fics = fics + result["src"] + config.LINE_END

		fics = fics + result["dst"] + config.SENTENCE_END

	return fics


def translate(filename, enattach, partition, fromLang, toLang):

	url = config.url_trans
	salt = random.randint(32768, 65536)

	text = common.readfile(filename)
	length = len(text)

	if partition == -1:
		partition = config.partition

	if fromLang == "":
		fromLang = config.fromLang

	if toLang == "":
		toLang = config.toLang

	# 如果长度不需要分段
	if length < partition:

		sign = init(text, config.appid, salt, config.secretKey)
		params = generateParams(text, fromLang, toLang, config.appid, salt, sign)

		results = getResponse(url, params)

		fics = generateResult(results, enattach)

	else:

		index = 0
		fics = ""

		# 当没有处理完所有的段落
		while index != -1:

			index_temp = text.find(config.ENTER, index + partition)

			if index_temp != -1:
				text_temp = text[index:index_temp]

			else:
				text_temp = text[index:length]

			sign = init(text_temp, config.appid, salt, config.secretKey)
			params = generateParams(text_temp, fromLang, toLang, config.appid, salt, sign)

			results = getResponse(url, params)

			fics = fics + generateResult(results, enattach)

			index = index_temp

	common.deletefile(filename)

	return fics
