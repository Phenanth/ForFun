# -*- coding: utf-8 -*-
import re
import requests

from . import preprocess
from . import translator

from docs import config


"""
core.py
~~~~~~~~~~~~~~~~~~~~~~~~

This module is the core of the downloader functions

"""

# ```````````````````````````````````````````````````

# 通过句子的结尾的符号判断是否是一个完整的句子
# 为了提高检测正确性，增加判定句子倒数第二个字符的逻辑
def isEndOfSentence(sentence):

	length = len(sentence)

	chara = sentence[length-1:length]
	chara2 = sentence[length-2:length-1]

	# 如果句子结尾是空格
	if chara == " ":
		# 如果倒数第二个字符是字母或者逗号
		if chara2.isalpha() or chara == "," or chara == " ":
			return False
		# 其他情况
		else:
			return True
	# 如果结尾是字母或者是逗号
	elif chara.isalpha() or chara == ",":
		return False
	# 其他情况
	else:
		return True

# 用于处理段落中的加粗文字的连接
def embedOperation(tmp, embed_str):

	flag = isEndOfSentence(tmp)

	# 有句子			
	if embed_str != "":
		# 是结尾
		if flag:
			tmp = embed_str + tmp +config.end_line
			embed_str = ""
		# 非结尾
		else:
			embed_str = embed_str + tmp
			tmp = ""
	# 无句子
	else:
		# 是结尾
		if flag:
			tmp = tmp + config.end_line
			embed_str = embed_str
		else:
			embed_str = tmp
			tmp = ""

	return tmp, embed_str

# 获取返回页面的text形式中的小说结点内容
def getRawText(url, cookies):

	page = requests.get(url, cookies=cookies)
	para = page.text

	index1 = para.find(config.string1)
	index2 = para.find(config.string2)

	subpara = config.tag_left +  para[index1:index2] + config.tag_right

	return rm(subpara)

# 去除特殊符号
def rm(text):

	rm = re.compile(u"\xa0")

	return rm.sub(" ", text)

# 去除结点内标签与 标签里的内容
def removePairs(text):

	if text:

		p = 0
		length = len(text)

		fics = ""
		embed_str = ""

		while p < length - config.charas_ignored:

			p = text.find(config.tag_right, p, length)
			q = text.find(config.tag_left, p, length)

			if p == -1 and q == -1:
				p = p + 10
				q = q + 10
				continue

			tmp = text[p + 1:q]

			if len(tmp) > 1:
				tmp, embed_str = embedOperation(tmp, embed_str)
				fics = fics + tmp

			p = q + 1

	return fics


# Downloader core function, main steps of the request dealing part
def downloader(requestBody):

	success = False
	attachment = ""

	# GENERATE & ADD parameters based on the original parameters
	url = preprocess.generate_url(requestBody["ficCode"], requestBody["ficIndex"])
	cookies = config.cookies
	
	# Get the text data and state code from the web API
	text = getRawText(url, cookies)

	fics = removePairs(text)
	
	# If successfully get the data from the Web API, operate it depends on the type of operation
	if len(fics) > 0:
		success = True

		attachment = preprocess.data_operation(fics, requestBody["operation"])
			
		if requestBody["translate"] == "trans":
			enattach = False
			if requestBody["enattach"] == "attach":
				enattach = True

			fics = translator.translate(config.directory_path + "/" + attachment, enattach)
			attachment = preprocess.data_operation(fics, requestBody["operation"])



	# For debugging and error handling, return all the processing data
	result = {
		"success": success,
		"body": requestBody,
		"attachment": attachment
	}
	
	return result
