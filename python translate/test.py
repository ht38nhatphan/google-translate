import googletrans
from googletrans import Translator
# print(googletrans.LANGUAGES)
t = Translator()
a= t.translate("dhdhd",src = "vi",dest = "en")

print(a.text)


