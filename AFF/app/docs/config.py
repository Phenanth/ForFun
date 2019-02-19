# -*- coding: utf-8 -*-
import sys, os


"""
Config.py

The global veriables are defined here.
"""

# `````````````````````````````````````````````````````
# Common

# Use this if you're running the server directly(python setup.py run)
# directory_path = os.path.abspath(os.path.join(os.sep, 'Users', 'Administrator', 'Documents', 'AFF_Downloader'))

# Use this if you're running server as a docker container(python setup.py docker)
directory_path = os.path.abspath(os.sep)

# The file path of README
README = 'README.md'


# ``````````````````````````````````````````````````````
# Downloader

# Cookie
cookies = dict(cookies_are="__cfduid=db6a38f42ec2cc7353f1be4a623bd00481548502011; _ga=GA1.2.228529505.1548502020; fitracking_6=no; rtk_gdpr_a=0; rtk_gdpr_c=JP; _pubcid=fee0db94-cdcf-42d1-830b-7f2e56164767; __gads=ID=e5a2fad591bc45d1:T=1548502036:S=ALNI_MYFeUVjfZJ4TNTLjJ8brvLbrvq8YQ; asianfanficspref=%7B%22siteversion%22%3A1%2C%22theme%22%3A%22blue%22%7D; csrf_aff_cookie=b52606222a943fd800067bcd1cd3e9a7; cmVsYXRl=93e817aa5f; _gid=GA1.2.308696800.1550480746; affsession=vl405akf286thrkp48ja0fvhe5frkr1c; YWN0aXZl=1")

# The common part of url path, the dashboard estat web api
url_path = "https://www.asianfanfics.com/story/view/"

string1 = "id=\"user-submitted-body\""
string2 = "id=\"chapter-upvote\""

tag_left = "<"
tag_right = ">"

# 忽视最后的n个文字，便于循环停止
charas_ignored = 30

end_line = "\n\n"


# ``````````````````````````````````````````````````````
# Translator

url_trans = "http://api.fanyi.baidu.com/api/trans/vip/translate"

LINE_END = "\n"
SENTENCE_END = "\n\n"

partition = 5000
ENTER = "\n"

fromLang = 'en'
toLang = 'zh'

# APP ID
appid = '20190212000265967'
# 密钥
secretKey = 'xbpxFLPvxh9MLMikS6sw'
