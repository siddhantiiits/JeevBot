from googletrans import Translator

def translate_text(text,destination_lang):
    translator = Translator()
    result = translator.translate(text,dest=destination_lang)

    return result.text

print(translate_text('Thanks for submission, *your registration will be confirmed by 6:30 .*\n\n*If you wish to un-register yourself anytime, Mail us at nandi.development@gmail.com*\n\n','hi'))