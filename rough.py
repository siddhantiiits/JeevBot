from googletrans import Translator


translator = Translator()
result = translator.translate('Mitä sinä teet',dest='hi')
print(result.text)