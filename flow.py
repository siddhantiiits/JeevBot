import requests
import os
import Registrations
import Animal_welfare
import functions
# l is the list corresponding to Dict[phone_num]
# incomingMsg is the incoming_msg


suffix_in_hindi = '\nहिंदी में भाषा बदलने के लिए कृपया *hindi* टाइप करें'
suffix_in_english = '\nTo change the language in English, please type *English*'
suffix_in_punjabi = '\nਭਾਸ਼ਾ ਨੂੰ ਪੰਜਾਬੀ ਵਿੱਚ ਬਦਲਣ ਲਈ *punjabi* ਟਾਈਪ ਕਰੋ'
suffix_eng = '\n\nSelect from the above options by typing number corresponding to the option.\n\nType *home* to go to main menu. \nType *back* to go back to previous menu.'
suffix_hin = '\n\nउपरोक्त विकल्पों में से विकल्प के अनुरूप संख्या टाइप करके चयन करें। \n\nमेन मेन्यू में जाने के लिए *home* टाइप करें। \nपिछले मेनू पर जाने के लिए *back* टाइप करें।'
suffix_punjabi = ' \n \n ਵਿਕਲਪ ਦੇ ਅਨੁਸਾਰੀ ਨੰਬਰ ਟਾਈਪ ਕਰਕੇ ਉਪਰੋਕਤ ਵਿਕਲਪਾਂ ਵਿੱਚੋਂ ਚੁਣੋ. \n\n ਮੁੱਖ ਮੀਨੂ ਤੇ ਜਾਣ ਲਈ *home* ਟਾਈਪ ਕਰੋ. \n ਪਿਛਲਾ ਮੀਨੂ ਤੇ ਜਾਣ ਲਈ *back* ਟਾਈਪ ਕਰੋ.'
def process(l,incomingMsg,mediaurl,phonenum,userName):

    mediaLink = ''
    mediaFlag = 0
    # print(l)
    if incomingMsg:
        if l == []:
            l.append('en')
        else:
            l.append(incomingMsg)
    else:
        if mediaurl:
            l.append(mediaurl)
    # print(l)

    if incomingMsg == 'home':
        lang_temp = l[0]
        l.clear()
        l.append(lang_temp)
    if incomingMsg == 'hindi':
        l.clear()
        l.append('hi')
    elif incomingMsg == 'english':
        l.clear()
        l.append('en')
    elif incomingMsg == 'punjabi':
        l.clear()
        l.append('pb')
    elif len(l) > 2 and incomingMsg == 'back':
        l.pop()
        l.pop()
    elif len(l) == 2 and incomingMsg == 'back':
        l.pop()


    # ----------------- Level 0 - Begin ---------------------

    if len(l) == 1:
        r = 'Hey! Am Nandi, how can I help you ? May I first know who\'s on the other side?\n\n' \
            'Please choose from the following options: \n\n' \
            '*Type 0 for veterinary hotline*\n\n' \
            '*1.* Pet Owner\n' \
            '*2.* Livestock / Poultry Owner\n' \
            '*3.* Para-Veterinarian\n' \
            '*4.* Veterinarian\n' \
            '*5.* Student\n' \
            '*6.* General Services\n'+ suffix_in_hindi+suffix_in_punjabi


        r_hindi = 'नमस्कार! मैं हूँ नंदी। मैं आपकी किस प्रसार सहायता कर सकता हूं? क्या मैं जान सकता हूं आप कौन हैं?\n\n' \
            'कृपया निम्नलिखित विकल्पों में से चुनें: \n\n' \
            '*पशु चिकित्सा हॉटलाइन के लिए 0 टाइप करें*\n\n' \
            '*1.* पालतू मालिक\n' \
            '*2.* पशुधन / कुक्कुट मालिक\n' \
            '*3.* पैरा-पशु चिकित्सक\n' \
            '*4.* पशु चिकित्सक\n' \
            '*5.* विद्यार्थी\n' \
            '*6.* सामान्य सेवाएं\n' + suffix_in_english+suffix_in_punjabi

        r_punjabi = 'ਸਤ ਸ੍ਰੀ ਅਕਾਲ! ਮੈਂ ਨੰਦੀ ਹਾਂ, ਮੈਂ ਤੁਹਾਡੀ ਕਿਵੇਂ ਮਦਦ ਕਰ ਸਕਦਾ ਹਾਂ? ਕੀ ਮੈਂ ਪਹਿਲਾਂ ਜਾਣ ਸਕਦਾ ਹਾਂ ਕਿ ਦੂਜੇ ਪਾਸੇ ਕੌਣ ਹੈ? \n \n '\
            'ਕਿਰਪਾ ਕਰਕੇ ਹੇਠ ਲਿਖੇ ਵਿਕਲਪਾਂ ਵਿੱਚੋਂ ਚੁਣੋ: \n \n'\
            '*ਵੈਟਰਨਰੀ ਹੌਟਲਾਈਨ ਲਈ 0 ਟਾਈਪ ਕਰੋ*\n \n'\
            '*1.* ਪਾਲਤੂ ਜਾਨਵਰ ਦਾ ਮਾਲਕ \n'\
            '*2.* ਪਸ਼ੂਧਨ / ਪੋਲਟਰੀ ਮਾਲਕ \n'\
            '*3.* ਪੈਰਾ-ਪਸ਼ੂ ਚਿਕਿਤਸਕ \n'\
            '*4.* ਪਸ਼ੂ ਚਿਕਿਤਸਕ \n'\
            '*5.* ਵਿਦਿਆਰਥੀ \n'\
            '*6.* ਆਮ ਸੇਵਾਵਾਂ \n' + suffix_in_english+suffix_in_hindi

    # ----------------- Level 0 - End ---------------------

    # ----------------- Level 1 - Begin ---------------------


    elif l[1:] == ['1']:
        r = 'Which pet do you own ?\n\n' \
            'Please choose from the following options: \n\n' \
            '*1.* Dog 🐶\n' \
            '*2.* Cat 🐈\n' \
            '*3.* Rabbit 🐰\n' \
            '*4.* Guinea Pig 🐭\n' \
            '*5.* Birds 🦜\n' \
            '*6.* Fishes 🐟\n' \
            '*7.* Other Exotic Species \n' + suffix_eng

        r_hindi = 'आपके पास कौन सा पालतू जानवर है?\n\n' \
            'कृपया निम्नलिखित विकल्पों में से चुनें: \n\n' \
            '*1.* कुत्ता 🐶\n' \
            '*2.* बिल्ली 🐈\n' \
            '*3.* खरगोश 🐰\n' \
            '*4.* गिनी पिग \n' \
            '*5.* पंछी \n' \
            '*6.* मछलियाँ 🐟\n' \
            '*7.* अन्य विदेशी प्रजातियां \n' + suffix_hin

    elif l[1:] == ['2']:
        r = 'Which animal do you own ?\n\n' \
            'Please choose from the following options: \n\n' \
            '*1.* Cattle and Buffalo 🐄\n' \
            '*2.* Pig 🐖\n' \
            '*3.* Horse 🐎\n' \
            '*4.* Camel 🐪\n' \
            '*5.* Sheep and Goat 🐑\n' \
            '*6.* Mithun 🐃\n' \
            '*7.* Yak\n' \
            '*8.* Poultry 🐓\n' + suffix_eng

        r_hindi = 'आपके पास कौनसा पशु है?\n\n' \
            'कृपया निम्नलिखित विकल्पों में से चुनें: \n\n' \
            '*1.* गाय या भैंस 🐄\n' \
            '*2.* सुअर 🐖\n' \
            '*3.* घोड़ा 🐎\n' \
            '*4.* ऊंट 🐪\n' \
            '*5.* भेड़ या बकरी 🐑\n' \
            '*6.* मिथुन \n' \
            '*7.* याक\n' \
            '*8.* कुक्कुट \n' + suffix_hin

        r_punjabi = 'ਤੁਸੀਂ ਕਿਹੜੇ ਪਾਲਤੂ ਜਾਨਵਰ ਦੇ ਮਾਲਕ ਹੋ? \n\n'\
            'ਕਿਰਪਾ ਕਰਕੇ ਹੇਠ ਲਿਖੇ ਵਿਕਲਪਾਂ ਵਿੱਚੋਂ ਚੁਣੋ: \n \n'\
            '*1.* ਗਾਂ ਅਤੇ ਮੱਝ 🐄 \n'\
            '*2.* ਸੂਰ 🐖 \n'\
            '*3.* ਘੋੜਾ 🐎 \n'\
            '*4.* ਊਠ 🐪 \n'\
            '*5.* ਭੇਡ ਅਤੇ ਬੱਕਰੀ 🐑 \n'\
            '*6.* ਮਿਥੁਨ 🐃 \n'\
            '*7.* ਯਾਕ \n'\
            '*8.* ਪੋਲਟਰੀ 🐓 \n' + suffix_punjabi

    elif l[1:] == ['3']:
        r = 'Hey Vet!\nWhat do you want ?\n\n' \
            'Please choose from the following options: \n\n' \
            '*1.* Want to Register yourself \n' \
            '*2.* Want Vaccination and Deworming Handbook \n' + suffix_eng

        r_hindi = 'All the above text in hindi' + suffix_hin

    elif l[1:] == ['4']:
        r = 'Hey Vet!\nWhat do you want ?\n\n' \
            'Please choose from the following options: \n\n' \
            '*1.* Want to Register yourself \n' \
            '*2.* Want Vaccination and Deworming Handbook \n' + suffix_eng

        r_hindi = 'All the above text in hindi' + suffix_hin

    elif l[1:] == ['5']:
        r = 'Hey Buddy!\nWhat do you want ?\n\n' \
            'Please choose from the following options: \n\n' \
            '*1.* Want Vaccination and Deworming Handbook \n' + suffix_eng

        r_hindi = 'अरे दोस्त!\nतुम क्या चाहते हो?\n\n' \
            'कृपया निम्नलिखित विकल्पों में से चुनें: \n\n' \
            '*1.* टीकाकरण और कृमि मुक्ति पुस्तिका \n' + suffix_hin


    elif l[1:] == ['6']:
        r = 'Which service do you want ?\n\n' \
            'Please choose from the following options: \n\n' \
            '*1.* Animal Insurance \n' \
            '*2.* Animal Adoption \n' \
            '*3.* Buy Pet \n' \
            '*4.* Anti-Animal Welfare Reporting \n' \
            '*5.* E-Platform for animal farmers \n' \
            '*6.* Mobile Applications \n' + suffix_eng

        r_hindi = 'आप कौन सी सेवा चाहते हैं?\n\n' \
            'कृपया निम्नलिखित विकल्पों में से चुनें: \n\n' \
            '*1.* पशु बीमा \n' \
            '*2.* पशु दत्तक ग्रहण \n' \
            '*3.* पालतू पशु खरीदें \n' \
            '*4.* पशु दुर्व्यवहार रिपोर्टिंग \n' \
            '*5.* पशु किसानों के लिए ई-प्लेटफॉर्म \n' \
            '*6.* मोबाइल एप्लिकेशन \n' + suffix_hin

        r_punjabi = 'ਤੁਸੀਂ ਕਿਹੜੀ ਸੇਵਾ ਚਾਹੁੰਦੇ ਹੋ? \n\n' \
            'ਕਿਰਪਾ ਕਰਕੇ ਹੇਠ ਲਿਖੇ ਵਿਕਲਪਾਂ ਵਿੱਚੋਂ ਚੁਣੋ: \n\n' \
            '*1.* ਪਸ਼ੂ ਬੀਮਾ \n' \
            '*2.* ਪਸ਼ੂ ਗੋਦ \n' \
            '*3.* ਇੱਕ ਪਾਲਤੂ ਜਾਨਵਰ ਖਰੀਦੋ \n'\
            '*4.* ਪਸ਼ੂ ਦੁਰਵਿਹਾਰ ਦੀ ਰਿਪੋਰਟਿੰਗ \n'\
            '*5.* ਪਸ਼ੂ ਪਾਲਕਾਂ ਲਈ ਈ-ਪਲੇਟਫਾਰਮ \n'\
            '*6.* ਮੋਬਾਈਲ ਐਪਲੀਕੇਸ਼ਨ \n' + suffix_punjabi
            

    # ----------------- Level 1 - End ---------------------

    # ----------------- Level 2 - Begin ---------------------



    elif l[1:] == ['1','1']:
        r = 'What service / info do you want for your Dog? 🐶\n\n' \
            'Please choose from the following options: \n\n' \
            '*1.* Vaccination 💉\n' \
            '*2.* Deworming 💊\n' \
            '*3.* Feed 🍲\n' \
            '*4.* Immunity Boosters 🍶\n' \
            '*5.* Boarding 🏡\n' \
            '*6.* Walking / Training \n' \
            '*7.* FAQs ❓\n' + suffix_eng

        r_hindi = 'आप अपने कुत्ते के लिए कौन सी सेवा/जानकारी चाहते हैं? 🐶\n\n' \
            'कृपया निम्नलिखित विकल्पों में से चुनें: \n\n' \
            '*1.* टीकाकरण 💉\n' \
            '*2.* कृमिनाशक 💊\n' \
            '*3.* फ़ीड 🍲\n' \
            '*4.* प्रतिरक्षा बूस्टर 🍶\n' \
            '*5.* बोर्डिंग 🏡\n' \
            '*6.* चलना/प्रशिक्षण \n' \
            '*7.* अक्सर पूछे जाने वाले प्रश्न ❓\n' + suffix_hin

    elif l[1:] == ['1','2']:
        r = 'What service / info do you want for your Cat? 🐈\n\n' \
            'Please choose from the following options: \n\n' \
            '*1.* Vaccination 💉\n' \
            '*2.* Deworming 💊\n' \
            '*3.* Feed 🍲\n' \
            '*4.* Immunity Boosters 🍶\n' \
            '*5.* Boarding 🏡\n' \
            '*6.* FAQs ❓\n' + suffix_eng

        r_hindi = 'आप अपनी बिल्ली के लिए कौन सी सेवा/जानकारी चाहते हैं? 🐈\n\n' \
            'कृपया निम्नलिखित विकल्पों में से चुनें: \n\n' \
            '*1.* टीकाकरण 💉\n' \
            '*2.* कृमिनाशक 💊\n' \
            '*3.* फ़ीड 🍲\n' \
            '*4.* प्रतिरक्षा बूस्टर 🍶\n' \
            '*5.* बोर्डिंग 🏡\n' \
            '*6.* अक्सर पूछे जाने वाले प्रश्न ❓\n' + suffix_hin

    elif l[1:] == ['1','3']:
        r = 'What service / info do you want for your Rabbit? 🐰\n\n' \
            'Please choose from the following options: \n\n' \
            '*1.* Vaccination 💉\n' \
            '*2.* Deworming 💊\n' \
            '*3.* Feed 🍲\n' \
            '*4.* FAQs ❓\n' + suffix_eng

        r_hindi = 'आप अपने खरगोश के लिए कौन सी सेवा/जानकारी चाहते हैं? 🐰\n\n' \
            'कृपया निम्नलिखित विकल्पों में से चुनें: \n\n' \
            '*1.* टीकाकरण 💉\n' \
            '*2.* कृमिनाशक 💊\n' \
            '*3.* फ़ीड 🍲\n' \
            '*4.* अक्सर पूछे जाने वाले प्रश्न ❓\n' + suffix_hin

    elif l[1:] == ['1','4']:
        r = 'What service / info do you want for your Guinea Pig? 🐭\n\n' \
            'Please choose from the following options: \n\n' \
            '*1.* Feed 🍲\n' \
            '*2.* FAQs ❓\n' + suffix_eng

        r_hindi = 'आप अपने गिनी पिग के लिए कौन सी सेवा/जानकारी चाहते हैं? 🐭\n\n' \
            'कृपया निम्नलिखित विकल्पों में से चुनें: \n\n' \
            '*1.* फ़ीड 🍲\n' \
            '*2.* अक्सर पूछे जाने वाले प्रश्न ❓\n' + suffix_hin

    elif l[1:] == ['2','1']:
        r = 'What service / info do you want for your Cattle / Buffalo? 🐄\n\n' \
            'Please choose from the following options: \n\n' \
            '*1.* Vaccination 💉\n' \
            '*2.* Deworming 💊\n' \
            '*3.* Feed 🍲\n' \
            '*4.* Foder 🍶\n' \
            '*5.* Others 🏡\n' \
            '*6.* Animal Tagging \n' \
            '*7.* ETT \n' \
            '*8.* Sex Sorted Semen \n' \
            '*9.* Semen Stations \n' + suffix_eng

        r_hindi = 'आप अपने गाय/भैंस के लिए क्या सेवा/जानकारी चाहते हैं? \n\n' \
            'कृपया निम्नलिखित विकल्पों में से चुनें: \n\n' \
            '*1.* टीकाकरण 💉\n' \
            '*2.* कृमिनाशक 💊\n' \
            '*3.* फ़ीड 🍲\n' \
            '*4.* चारा 🍶\n' \
            '*5.* अन्य 🏡\n' \
            '*6.* पशु टैगिंग \n' \
            '*7.* ई टी टी \n' \
            '*8.* लिंग क्रमबद्ध वीर्य \n' \
            '*9.* वीर्य स्टेशन \n' + suffix_hin

        r_punjabi = 'ਤੁਸੀਂ ਆਪਣੇ ਗਾਂ / ਮੱਝ ਲਈ ਕਿਹੜੀ ਸੇਵਾ / ਜਾਣਕਾਰੀ ਚਾਹੁੰਦੇ ਹੋ? \n \n '\
            'ਕਿਰਪਾ ਕਰਕੇ ਹੇਠ ਲਿਖੇ ਵਿਕਲਪਾਂ ਵਿੱਚੋਂ ਚੁਣੋ: \n \n'\
            '*1.* ਟੀਕਾਕਰਣ  \n'\
            '*2.* ਕੀਟਾਣੂ ਰਹਿਤ 💊 \n'\
            '*3.* ਫੀਡ 🍲 \n'\
            '*4.* ਚਾਰਾ 🍶 \n'\
            '*5.* ਹੋਰ 🏡 \n'\
            '*6.* ਪਸ਼ੂ ਟੈਗਿੰਗ  \n'\
            '*7.* ਈ ਟੀ ਟੀ \n'\
            '*8.* ਲਿੰਗ ਕ੍ਰਮਬੱਧ ਵੀਰਜ \n'\
            '*9.* ਵੀਰਜ ਸਟੇਸ਼ਨ \n' + suffix_punjabi

    elif l[1:] == ['2','2']:
        r = 'What service / info do you want for your Pig? 🐖\n\n' \
            'Please choose from the following options: \n\n' \
            '*1.* Vaccination 💉\n' \
            '*2.* Deworming 💊\n' \
            '*3.* Feed 🍲\n' \
            '*4.* Immunity and Health Boosters 🍶\n' + suffix_eng

        r_hindi = 'आप अपने सूकर के लिए कौन सी सेवा/जानकारी चाहते हैं? 🐖\n\n' \
            'कृपया निम्नलिखित विकल्पों में से चुनें: \n\n' \
            '*1.* टीकाकरण 💉\n' \
            '*2.* कृमिनाशक \n' \
            '*3.* फ़ीड 🍲\n' \
            '*4.* प्रतिरक्षा और स्वास्थ्य बूस्टर 🍶\n' + suffix_hin

    elif l[1:] == ['2','3']:
        r = 'What service / info do you want for your Horse? 🐎\n\n' \
            'Please choose from the following options: \n\n' \
            '*1.* Vaccination 💉\n' \
            '*2.* Deworming 💊\n' \
            '*3.* Feed 🍲\n' \
            '*4.* Immunity and Health Boosters 🍶\n' + suffix_eng

        r_hindi = 'आप अपने घोड़े के लिए कौन सी सेवा/जानकारी चाहते हैं? 🐎\n\n' \
            'कृपया निम्नलिखित विकल्पों में से चुनें: \n\n' \
            '*1.* टीकाकरण 💉\n' \
            '*2.* कृमिनाशक \n' \
            '*3.* फ़ीड 🍲\n' \
            '*4.* प्रतिरक्षा और स्वास्थ्य बूस्टर 🍶\n' + suffix_hin

    elif l[1:] == ['2','4']:
        r = 'What service / info do you want for your Camel? 🐪\n\n' \
            'Please choose from the following options: \n\n' \
            '*1.* Vaccination 💉\n' \
            '*2.* Deworming 💊\n' \
            '*3.* Feed 🍲\n' \
            '*4.* Immunity and Health Boosters 🍶\n' + suffix_eng

        r_hindi = 'आप अपने ऊंट के लिए कौन सी सेवा/जानकारी चाहते हैं? 🐪\n\n' \
            'कृपया निम्नलिखित विकल्पों में से चुनें: \n\n' \
            '*1.* टीकाकरण 💉\n' \
            '*2.* कृमिनाशक \n' \
            '*3.* फ़ीड 🍲\n' \
            '*4.* प्रतिरक्षा और स्वास्थ्य बूस्टर 🍶\n' + suffix_hin

    elif l[1:] == ['2','5']:
        r = 'What service / info do you want for your Sheep and Goat? 🐑\n\n' \
            'Please choose from the following options: \n\n' \
            '*1.* Vaccination 💉\n' \
            '*2.* Deworming 💊\n' \
            '*3.* Feed 🍲\n' \
            '*4.* Immunity and Health Boosters 🍶\n' + suffix_eng

        r_hindi = 'आप अपनी भेड़ और बकरी के लिए क्या सेवा/जानकारी चाहते हैं? 🐑\n\n' \
            'कृपया निम्नलिखित विकल्पों में से चुनें: \n\n' \
            '*1.* टीकाकरण 💉\n' \
            '*2.* कृमिनाशक \n' \
            '*3.* फ़ीड 🍲\n' \
            '*4.* प्रतिरक्षा और स्वास्थ्य बूस्टर 🍶\n' + suffix_hin

    elif l[1:] == ['2','6']:
        r = 'What service / info do you want for your Mithun? 🐃\n\n' \
            'Please choose from the following options: \n\n' \
            '*1.* Vaccination 💉\n' \
            '*2.* Deworming 💊\n' \
            '*3.* Feed 🍲\n' \
            '*4.* Immunity and Health Boosters 🍶\n' + suffix_eng

        r_hindi = 'आप अपने मिथुन के लिए कौन सी सेवा/जानकारी चाहते हैं? 🐃\n\n' \
            'कृपया निम्नलिखित विकल्पों में से चुनें: \n\n' \
            '*1.* टीकाकरण 💉\n' \
            '*2.* कृमिनाशक \n' \
            '*3.* फ़ीड 🍲\n' \
            '*4.* प्रतिरक्षा और स्वास्थ्य बूस्टर 🍶\n' + suffix_hin

    elif l[1:] == ['2','7']:
        r = 'What service / info do you want for your Yak? \n\n' \
            'Please choose from the following options: \n\n' \
            '*1.* Vaccination 💉\n' \
            '*2.* Deworming 💊\n' \
            '*3.* Feed 🍲\n' \
            '*4.* Immunity and Health Boosters 🍶\n' + suffix_eng

        r_hindi = 'आप अपने याक के लिए क्या सेवा/जानकारी चाहते हैं? \n\n' \
            'कृपया निम्नलिखित विकल्पों में से चुनें: \n\n' \
            '*1.* टीकाकरण 💉\n' \
            '*2.* कृमिनाशक \n' \
            '*3.* फ़ीड 🍲\n' \
            '*4.* प्रतिरक्षा और स्वास्थ्य बूस्टर 🍶\n' + suffix_hin

    elif l[1:] == ['2','8']:
        r = 'What service / info do you want for your Poultry? 🐓\n\n' \
            'Please choose from the following options: \n\n' \
            '*1.* Vaccination 💉\n' \
            '*2.* Deworming 💊\n' \
            '*3.* Feed 🍲\n' \
            '*4.* Immunity and Health Boosters 🍶\n' + suffix_eng

        r_hindi = 'आप अपने पोल्ट्री के लिए कौन सी सेवा/जानकारी चाहते हैं? 🐓\n\n' \
            'कृपया निम्नलिखित विकल्पों में से चुनें: \n\n' \
            '*1.* टीकाकरण 💉\n' \
            '*2.* कृमिनाशक \n' \
            '*3.* फ़ीड 🍲\n' \
            '*4.* प्रतिरक्षा और स्वास्थ्य बूस्टर 🍶\n' + suffix_hin

    elif l[1:] == ['4','1']:
        r = 'To get yourself registered as a veterinarian, fill the form {form link} or you can register by ' \
            'sending your details in this format: \n\n' \
            'Your Name\n' \
            'Registration Number\n' \
            'Phone Number\n' \
            'Address\n' \
            'City\n' \
            'State\n' \
            'Pincode\n\n' \
            'For Example: \n' \
            '*Sherlock Holmes*\n' \
            '*PCVET54YZ3498*\n' \
            '*+9120392949393*\n' \
            '*221 Bakers Street*\n' \
            '*Mumbai*\n' \
            '*Maharashtra*\n' \
            '*123456*\n\n' + suffix_eng

        r_hindi = 'स्वयं को पशु चिकित्सक के रूप में पंजीकृत कराने के लिए, फॉर्म {फॉर्म लिंक} भरें या ' \
            'आप इस प्रारूप में अपना विवरण भेजकर पंजीकरण कर सकते हैं:\n\n'\
            'आपका नाम\n' \
            'पंजीकरण संख्या\n' \
            'फ़ोन नंबर\n' \
            'पता\n' \
            'शहर\n' \
            'राज्य\n' \
            'पिनकोड\n\n' \
            'उदाहरण के लिए: \n' \
            '*शर्लक होम्स*\n' \
            '*पीसीवीईटी54वाईजेड3498*\n' \
            '*+9120392949393*\n' \
            '*221 बेकर्स स्ट्रीट*\n' \
            '*मुंबई*\n' \
            '*महाराष्ट्र*\n' \
            '*123456*\n\n' + suffix_hin


    elif l[1:] == ['6','5']:
        r = 'What E-Platform do you want to try? \n\n' \
            'Here\'s the List of all available platforms with their Links: \n\n' \
            '*1.* Kisan Sarthi ' \
            '(https://kisansarathi.in)\n'\
            '*2.* Kisan Mitr ' \
            '(https://kisanmitr.gov.in)\n'\
            '*3.* Farmer Portal of India ' \
            '(https://farmer.gov.in)\n'\
            '*4.* DAHD '\
            '(https://dahd.nic.in)\n' + suffix_eng

        r_hindi = 'आप कौन सा ई-प्लेटफ़ॉर्म आज़माना चाहते हैं? \n\n' \
            'यहाँ\'उनके लिंक के साथ सभी उपलब्ध प्लेटफ़ॉर्म की सूची: \n\n' \
            '*1.* किसान सारथी' \
            '(https://kisansarathi.in)\n'\
            '*2.* किसान मित्र' \
            '(https://kisanmitr.gov.in)\n'\
            '*3.* भारत का किसान पोर्टल' \
            '(https://farmer.gov.in)\n'\
            '*4.* डीएएचडी'\
            '(https://dahd.nic.in)\n' + suffix_hin

    elif l[1:] == ['6','6']:
        r = 'What Mobile Application do you want to try? \n\n' \
            'Here\'s the List of all available apps with their Links: \n\n' \
            '*1.* E-Gopala ' \
            '(https://play.google.com/store/apps/details?id=coop.nddb.pashuposhan&hl=en_IN&gl=US)\n'  + suffix_eng

        r_hindi = 'आप कौन सा मोबाइल एप्लिकेशन आजमाना चाहते हैं? \n\n' \
            'यहां सभी उपलब्ध ऐप्स की सूची उनके लिंक के साथ है: \n\n' \
            '*1.* ई-गोपाल' \
            '(https://play.google.com/store/apps/details?id=coop.nddb.pashuposhan&hl=hi_IN&gl=US)\n' + suffix_hin

    elif l[1:] in ( ['5', '1'], ['4','2'],['3','2']):
        r = 'Here is your vaccination Guide \n\n' + suffix_eng
        mediaLink = 'https://firebasestorage.googleapis.com/v0/b/nandi-2adc2.appspot.com/o/Vaccination_Charts%2FVaccination_Handbook.pdf?alt=media&token=4044d13e-3691-4e86-9ef6-c4e6f023bb79'
        r_hindi = 'ये है आपकी टीकाकरण गाइड \n\n' + suffix_hin
        mediaFlag = 1

    # -------------------------Animal Welfare----------------------------

    elif l[1:] == ['6','4']:
        r= "*Send us an image/ video depicting Animal abuse/ anti- animal welfare.* \n\n"

        r_hindi = "*हमें पशु दुर्व्यवहार/पशु-विरोधी कल्याण को दर्शाने वाली एक छवि/वीडियो भेजें।* \n\n"

    elif l[1:3] == ['6', '4'] and len(l) == 4:
        r = "*Thanks! Write a short description for the image/ video you sent.*"
        r_hindi = "*धन्यवाद! आपके द्वारा भेजी गई छवि/वीडियो के लिए एक संक्षिप्त विवरण लिखें।*"
    elif l[1:3] == ['6', '4'] and len(l) == 5:
        r = "Share the exact location of site, or type in exact address of site with pincode."
        r_hindi = "साइट का सटीक स्थान साझा करें, या पिनकोड के साथ साइट का सटीक पता लिखें।"
    elif l[1:3] == ['6', '4'] and len(l) == 6:
        print(l[5])
        r,r_hindi = Animal_welfare.animalWelfare(l[3],l[4],phonenum,userName,l[5],l[5])

    #     here func will return both r and r_hindi itself. No need to add here







    # -------------------------Animal Welfare----------------------------




        # print('lolo')
        # if mediaurl:
        #     print('hiii')
        #     r = requests.get(mediaurl)
        #     content_type = r.headers['Content-Type']
        #     username = 'user'
        #     message = 'pp'
        #     if content_type == 'image/jpeg':
        #         filename = f'uploads/{username}/{message}.jpg'
        #     elif content_type == 'image/png':
        #         filename = f'uploads/{username}/{message}.png'
        #     elif content_type == 'image/gif':
        #         filename = f'uploads/{username}/{message}.gif'
        #     else:
        #         filename = None
        #     if filename:
        #         if not os.path.exists(f'uploads/{username}'):
        #             os.mkdir(f'uploads/{username}')
        #         with open(filename, 'wb') as f:
        #             print(r.content)
        #             f.write(r.content)
        #             print("Done")
        #         r = "Thankyou! Your image is recieved and we are working on it!"
        #     else:
        #         r = 'The file that you submitted is not a supported image type.'
        # else:
        #     r = 'Please send an image!'



    # ----------------- Level 2 - End ---------------------


    # ----------------- Level 3 - Begin ---------------------
        # Update their charts location

    elif l[1:] == ['2','1','1']:
        r = 'Here\'s the vaccination chart 🎉\n\n' \
            'Nearest Vaccination Centers - *Feature Coming Soon\n*' + suffix_eng
        r_hindi = 'ये रहा टीकाकरण चार्ट 🎉\n\n' \
            'निकटतम टीकाकरण केंद्र - *सुविधा जल्द आ रही है\n*' + suffix_hin
        mediaLink = 'https://firebasestorage.googleapis.com/v0/b/nandi-2adc2.appspot.com/o/Vaccination_Charts%2FVaccinationChart_CattleandBuffalo.png?alt=media&token=6a75acdb-3544-42d2-be4f-ea89b6f5e50c'
        mediaFlag = 1
    elif l[1:] == ['2', '2', '1']:
        r = 'Here\'s the vaccination chart 🎉\n\n' \
            'Nearest Vaccination Centers - *Feature Coming Soon\n*' + suffix_eng
        r_hindi = 'ये रहा टीकाकरण चार्ट 🎉\n\n' \
            'निकटतम टीकाकरण केंद्र - *सुविधा जल्द आ रही है\n*' + suffix_hin
        mediaLink = 'https://firebasestorage.googleapis.com/v0/b/nandi-2adc2.appspot.com/o/Vaccination_Charts%2FVaccinationChart_Pig.png?alt=media&token=30a4fbd8-af25-4b3a-90e7-06ddec1a27eb'
        mediaFlag = 1
    elif l[1:] == ['2', '3', '1']:
        r = 'Here\'s the vaccination chart 🎉\n\n' \
            'Nearest Vaccination Centers - *Feature Coming Soon\n*' + suffix_eng
        r_hindi = 'ये रहा टीकाकरण चार्ट 🎉\n\n' \
            'निकटतम टीकाकरण केंद्र - *सुविधा जल्द आ रही है\n*' + suffix_hin
        mediaLink = 'https://firebasestorage.googleapis.com/v0/b/nandi-2adc2.appspot.com/o/Vaccination_Charts%2FVaccinationChart_Horse.png?alt=media&token=22192e19-e143-4d68-8bb1-3e5e127f9b8a'
        mediaFlag = 1
    elif l[1:] == ['2', '4', '1']:
        r = 'Here\'s the vaccination chart 🎉\n\n' \
            'Nearest Vaccination Centers - *Feature Coming Soon\n*' + suffix_eng
        r_hindi = 'ये रहा टीकाकरण चार्ट 🎉\n\n' \
            'निकटतम टीकाकरण केंद्र - *सुविधा जल्द आ रही है\n*' + suffix_hin
        mediaLink = 'https://firebasestorage.googleapis.com/v0/b/nandi-2adc2.appspot.com/o/Vaccination_Charts%2FVaccinationChart_Camel.png?alt=media&token=aecf6368-6b53-4b1c-881f-3fdc026c635e'
        mediaFlag = 1
    elif l[1:] == ['2', '5', '1']:
        r = 'Here\'s the vaccination chart 🎉\n\n' \
            'Nearest Vaccination Centers - *Feature Coming Soon\n*' + suffix_eng
        r_hindi = 'ये रहा टीकाकरण चार्ट 🎉\n\n' \
            'निकटतम टीकाकरण केंद्र - *सुविधा जल्द आ रही है\n*' + suffix_hin
        mediaLink = 'https://firebasestorage.googleapis.com/v0/b/nandi-2adc2.appspot.com/o/Vaccination_Charts%2FVaccinationChart_SheepandGoat.png?alt=media&token=94081d27-eb30-4c12-ac58-d3b86ca02bfe'
        mediaFlag = 1
    elif l[1:] == ['2', '6', '1']:
        r = 'Here\'s the vaccination chart🎉\n\n' \
            'Nearest Vaccination Centers - *Feature Coming Soon\n*' + suffix_eng
        r_hindi = 'ये रहा टीकाकरण चार्ट 🎉\n\n' \
            'निकटतम टीकाकरण केंद्र - *सुविधा जल्द आ रही है\n*' + suffix_hin
        mediaLink = 'https://firebasestorage.googleapis.com/v0/b/nandi-2adc2.appspot.com/o/Vaccination_Charts%2FVaccinationChart_Mithun.png?alt=media&token=b71ef7ba-2245-4b09-87a3-a327a4db49df'
        mediaFlag = 1
    elif l[1:] == ['2', '7', '1']:
        r = 'Here\'s the vaccination chart🎉\n\n' \
            'Nearest Vaccination Centers - *Feature Coming Soon\n*' + suffix_eng
        r_hindi = 'ये रहा टीकाकरण चार्ट 🎉\n\n' \
            'निकटतम टीकाकरण केंद्र - *सुविधा जल्द आ रही है\n*' + suffix_hin
        mediaLink = 'https://firebasestorage.googleapis.com/v0/b/nandi-2adc2.appspot.com/o/Vaccination_Charts%2FVaccinationChart_Yak.png?alt=media&token=ccd0b9fc-789c-4cbc-9183-305ad0b675f9'
        mediaFlag = 1
    elif l[1:] == ['2', '8', '1']:
        r = 'Vaccination Chart coming soon' \
            'Nearest Vaccination Centers - *Feature Coming Soon\n*' + suffix_eng
        r_hindi = 'ये रहा टीकाकरण चार्ट 🎉\n\n' \
            'निकटतम टीकाकरण केंद्र - *सुविधा जल्द आ रही है\n*' + suffix_hin
        # mediaLink = 'https://firebasestorage.googleapis.com/v0/b/nandi-2adc2.appspot.com/o/Vaccination_Charts%2FVaccinationChart_Dog.png?alt=media&token=48bd47c0-70b2-4a59-8851-a8857f99b999'
        mediaFlag = 0



    elif l[1:] == ['1','1','1']:
        r = 'Here\'s the vaccination chart for your dog ! 🎉\n\n' \
            'Nearest Vaccination Centers - *Feature Coming Soon\n*' + suffix_eng
        r_hindi = 'ये रहा आपके कुत्ते के लिए टीकाकरण चार्ट ! 🎉\n\n' \
            'निकटतम टीकाकरण केंद्र - *सुविधा जल्द आ रही है\n*' + suffix_hin
        mediaLink = 'https://firebasestorage.googleapis.com/v0/b/nandi-2adc2.appspot.com/o/Vaccination_Charts%2FVaccinationChart_Dog.png?alt=media&token=48bd47c0-70b2-4a59-8851-a8857f99b999'
        mediaFlag = 1

    elif l[1:] == ['1','2','1']:
        r = 'Here\'s the vaccination chart for your cat ! 🎉\n\n' \
            'Nearest Vaccination Centers - *Feature Coming Soon\n*' + suffix_eng
        r_hindi = 'ये रहा आपकी बिल्ली के लिए टीकाकरण चार्ट ! 🎉\n\n' \
            'निकटतम टीकाकरण केंद्र - *सुविधा जल्द आ रही है\n*' + suffix_hin
        mediaLink = 'https://firebasestorage.googleapis.com/v0/b/nandi-2adc2.appspot.com/o/Vaccination_Charts%2FVaccinationChart_Cat.png?alt=media&token=89e80cae-b922-42d9-9f72-4291672a9ffd'
        mediaFlag = 1

    elif l[1:] == ['1','3','1']:
        r = 'Coming Soon'
        r_hindi = 'All the above text in hindi' + suffix_hin
        # mediaLink = 'https://firebasestorage.googleapis.com/v0/b/jeevbot.appspot.com/o/dogvcc.jpg?alt=media&token=b2e7e0d5-092f-436c-af20-ee7f0affd90c'
        mediaFlag = 0


    elif l[1:-1] == ['4','1']:
        print(l[-1])

        name,registration_number,phone_number,address,city,state,pincode = map(str,l[-1].split('\n'))
        r,r_hindi = Registrations.registerVeterinarian(name,registration_number,phone_number,address,city,state,pincode)

        #     here func will return both r and r_hindi itself. No need to add here




    



    # ----------------- Level 3 - End ---------------------


    else:
        r = 'You have either entered an invalid response or this feature is under development'
        l.pop()
        mediaLink = ''
        mediaFlag = 0



    #
    # if l[0] == 'hi':
    #     r = functions.translate_text(r,destination_lang='hi')
    #
    # if len(l)==1 and l[0] == 'hi':
    #     r += suffix_in_english
    # elif len(l)==1 and l[0] == 'en':
    #     r += suffix_in_hindi
    #
    # elif suffixFlag and l[0]=='hi':
    #     r += suffix_hin
    # elif suffixFlag and l[0]=='en':
    #     r += suffix_eng



    # Uncomment the code below
    if l[0] == 'hi':
        r = r_hindi
    elif l[0] == 'pb':
        r = r_punjabi



    return r,mediaLink,mediaFlag


