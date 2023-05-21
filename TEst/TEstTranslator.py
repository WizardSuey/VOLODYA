from translate import Translator

translator = Translator(from_lang="ru", to_lang="en")
text = str(input())

end_text = translator.translate(text)
print(end_text)