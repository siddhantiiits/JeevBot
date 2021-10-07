from googletrans import Translator

def translate_text(text,destination_lang):
    translator = Translator()
    result = translator.translate(text,dest=destination_lang)

    return result.text

print(translate_text('Type *home* to go to main menu','hi'))