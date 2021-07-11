# import googletrans
from googletrans import Translator
# print(googletrans.LANGUAGES)
t = Translator()
# a= t.translate("đẹp trai",src = "vi",dest = "en")
a = t.translate('안녕하세요.')
print(a.text)


