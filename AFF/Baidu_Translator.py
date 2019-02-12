"""
百度翻译小脚本
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
没什么好说的，调用一下百度翻译而已。

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

line_end = "\n"
sentence_end = "\n\n"


# ``````````````````````````````````````````````````````````````

def readFile(filename):

	with open(filename, "r", encoding="utf-8") as f:
		text = f.read()

	return text

def init(appid, salt, secretKey):

	text = readFile(filename)

	sign = appid + text + str(salt) + secretKey
	m1 = hashlib.md5()
	m1.update(sign.encode("utf-8"))
	sign = m1.hexdigest()

	return text, sign

def generateParams(text, fromLang, toLang, appid, salt, sign):

	params = {}

	params.update({"q": text})
	params.update({"from": fromLang})
	params.update({"to": toLang})
	params.update({"appid": appid})
	params.update({"salt": salt})
	params.update({"sign": sign})

	return params

def getResult(url, params):

	return requests.get(url, params).json()["trans_result"]

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

text, sign = init(appid, salt, secretKey)
params = generateParams(text, fromLang, toLang, appid, salt, sign)

results = getResult(url, params)

fics = ""
for result in results:
	# 双语开关为开
	if isEnAdded:
		fics = fics + result["src"] + line_end

	fics = fics + result["dst"] + sentence_end

saveFile(fics, filename_save)
