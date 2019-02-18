"""
百度翻译小脚本
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
没什么好说的，调用一下百度翻译而已。

* 更新了根据文章长度分段翻译的功能

[百度翻译API首页](http://api.fanyi.baidu.com/api/trans/product/index)
"""
import requests
import random
import hashlib

# 双语开关
isEnAdded = True

filename = "fics.txt"
filename_save = "fics_CN.txt"

url = "http://api.fanyi.baidu.com/api/trans/vip/translate"

LINE_END = "\n"
SENTENCE_END = "\n\n"

partition = 5000
ENTER = "\n"


# ``````````````````````````````````````````````````````````````

def readFile(filename):

	with open(filename, "r", encoding="utf-8") as f:
		text = f.read()

	return text

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

def generateResult(results):

	fics = ""

	for result in results:
		# 双语开关为开
		if isEnAdded:
			fics = fics + result["src"] + LINE_END

		fics = fics + result["dst"] + SENTENCE_END

	return fics

def saveFile(text, file_name_save):

	with open(file_name_save, "w", encoding="utf-8") as f:
		f.write(text)

# ``````````````````````````````````````````````````````````````


fromLang = 'en'
toLang = 'zh'
salt = random.randint(32768, 65536)

# APP ID
appid = ''
# 密钥
secretKey = ''

text = readFile(filename)
length = len(text)

# 如果长度不需要分段
if length < partition:

	sign = init(text, appid, salt, secretKey)
	params = generateParams(text, fromLang, toLang, appid, salt, sign)

	results = getResponse(url, params)

	fics = generateResult(results)

else:

	index = 0
	fics = ""

	# 当没有处理完所有的段落
	while index != -1:

		index_temp = text.find(ENTER, index + partition)

		if index_temp != -1:
			text_temp = text[index:index_temp]

		else:
			text_temp = text[index:length]

		sign = init(text_temp, appid, salt, secretKey)
		params = generateParams(text_temp, fromLang, toLang, appid, salt, sign)

		results = getResponse(url, params)

		fics = fics + generateResult(results)

		index = index_temp

# 储存翻译结果
saveFile(fics, filename_save)
