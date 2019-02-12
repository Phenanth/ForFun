"""
AFF文章下载小脚本
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
后来又想到的一个处理方法看起来是下载AFF上面的文章的一个通用的方法。
这个下载只支持下载能够用浏览器看到全文的小说，需要登陆用的cookie

算法说明：
算法很简单，就两步：
1. 获得页面内容的string形式
2. 去掉"<"和">"以及之间的内容

使用说明：
1. 修改变量部分的url和cookie，更换成想要下载的小说的链接和登陆账号的cookie
2. 在命令行输入`python (脚本名).py`

注意事项：
- 不知道自己的cookie的话，在浏览器的发送headers里看就可以了
- 如果下载内容不正确的话，检查以下事项：
	+ 网络连接是否正常
	+ cookie是否过期
	+ 使用的cookie的帐号在浏览器登录的情况下是否能够看到完整的小说内容（Subscribe/Group Member）

"""

import requests
from lxml import html

# 小说地址
url = ""
# 登录产生的Cookie
cookies = dict(cookies_are="")

# 保存的文件名
file_name = "fics.txt"

string1 = "id=\"user-submitted-body\""
string2 = "id=\"chapter-upvote\""

tag_left = "<"
tag_right = ">"

# 忽视最后的n个文字，便于循环停止
charas_ignored = 30

end_line = "\n\n"


# ```````````````````````````````````````````````````

# 通过句子的结尾的符号判断是否是一个完整的句子
# 为了提高检测正确性，增加判定句子倒数第二个字符的逻辑
def isEndOfSentence(sentence):

	length = len(sentence)

	chara = sentence[length-1:length]
	chara2 = sentence[length-2:length-1]

	# 如果句子结尾是空格
	if chara == "":
		# 如果倒数第二个字符是字母或者逗号
		if chara2.isalpha() or chara == ",":
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
			tmp = embed_str + tmp +end_line
			embed_str = ""
		# 非结尾
		else:
			embed_str = embed_str + tmp
			tmp = ""
	# 无句子
	else:
		# 是结尾
		if flag:
			tmp = tmp + end_line
			embed_str = embed_str
		else:
			embed_str = tmp
			tmp = ""

	return tmp, embed_str

# 获取返回页面的text形式中的小说结点内容
def getRawText(url, cookies):

	page = requests.get(url, cookies=cookies)
	para = page.text

	index1 = para.find(string1)
	index2 = para.find(string2)

	subpara = tag_left +  para[index1:index2] + tag_right

	return subpara

# 去除结点内标签与标签里的内容
def removePairs(text):

	if text:

		p = 0
		length = len(text)

		fics = ""
		embed_str = ""

		while p < length - charas_ignored:

			p = text.find(tag_right, p, length)
			q = text.find(tag_left, p, length)

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

# 保存文件
def saveFile(text, file_name):

	with open(file_name, "w", encoding="utf-8") as f:
		f.write(text)


# ```````````````````````````````````````````````````


print("Started downloading fics, please wait... ;3")

text = getRawText(url, cookies)

fics = removePairs(text)

saveFile(fics, file_name)

print("Succussfully downloaded fics, enjoy!!! =)")
