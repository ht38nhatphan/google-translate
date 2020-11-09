import googletrans
from googletrans import Translator
# print(googletrans.LANGUAGES)
t = Translator()
a= t.translate("dung",src = "vi",dest = "en")

print(a.text)


