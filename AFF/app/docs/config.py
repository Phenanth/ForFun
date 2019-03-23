# -*- coding: utf-8 -*-
import sys, os


"""
Config.py

The global veriables are defined here.
"""

# `````````````````````````````````````````````````````
# Common

# Use this if you're running the server directly(python setup.py run)
directory_path = os.path.abspath(os.path.join(os.sep, 'Users', 'Administrator', 'Documents', 'AFF_Downloader'))

# Use this if you're running server as a docker container(python setup.py docker)
# directory_path = os.path.abspath(os.path.join(os.sep, "root", "Documents", "AFF_Downloader"))

# directory_path = os.path.abspath(os.path.join(os.sep, "home", "skhr-0324", "project", "data", "AFF_Downloader"))

# The file path of README
README = 'README.md'


# ``````````````````````````````````````````````````````
# Downloader

# Cookie
cookies = dict(cookies_are="__cfduid=db6a38f42ec2cc7353f1be4a623bd00481548502011; _ga=GA1.2.228529505.1548502020; rtk_gdpr_a=0; rtk_gdpr_c=JP; _pubcid=fee0db94-cdcf-42d1-830b-7f2e56164767; __gads=ID=e5a2fad591bc45d1:T=1548502036:S=ALNI_MYFeUVjfZJ4TNTLjJ8brvLbrvq8YQ; cmVsYXRl=93e817aa5f; YWN0aXZl=1; asianfanficspref=%7B%22siteversion%22%3A1%2C%22theme%22%3A%22blackwhite%22%7D; fitracking_6=yes; fiTrackingDomainParams=%7B%22host%22%3A%22tracking1.firstimpression.io%22%2C%22type%22%3A%22full%22%7D; csrf_aff_cookie=e023a7464b6ce41f4fbb0efdef955401; _gid=GA1.2.2137991285.1553315043; affsession=kl767thiefi03c5eu614krj312cd2ama; _pk_ses.6574.3985=*; fi_utm=direct%7Cdirect%7C%7C%7C%7C; _pk_id.6574.3985=1b54e8d0f1f6e015.1551360924.8.1553315944.1553315062.")

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
# Translator Default Params

url_trans = "http://api.fanyi.baidu.com/api/trans/vip/translate"

LINE_END = "\n"
SENTENCE_END = "\n\n"

partition = 3000
ENTER = "\n"

fromLang = 'en'
toLang = 'zh'

# APP ID
appid = '20190212000265967'
# Sub APP ID
# appid = '20190221000269592'
# Secret Key
secretKey = 'xbpxFLPvxh9MLMikS6sw'
# Sub Secret Key
# secretKey = 'EMzCxdhMSlN812I7M1GC'
