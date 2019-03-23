from googletrans import Translator

# Read a file and return its contents
def readfile(file_path):

    with open(file_path, "r", encoding="utf-8") as f:
        texts = f.read()

    return texts

def generateResultsGoogle(fics, texts, enttach):
	if enttach:
		fics = texts + fics

	return fics

Translation = Translator()

partition = 3000

fics = ""
text = readfile("fics.txt")
length = len(text)

if length < partition:
		results = Translation.translate(text, src='en', dest='zh-CN').text
		fics = results

else:

	index = 0
	fics = ""

	# 当没有处理完所有的段落
	while index != -1:

		index_temp = text.find("\n", index + partition)

		if index_temp != -1:
			text_temp = text[index:index_temp]

		else:
			text_temp = text[index:length]

		results = Translation.translate(text_temp, src='en', dest='zh-CN').text

		fics = fics + results

		index = index_temp



# resutl = Translator.translate(text, src="en", dest="zh-CN")

print(generateResultsGoogle(fics, text, 1))