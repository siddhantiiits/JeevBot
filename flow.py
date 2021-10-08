import requests
import os
import Registrations
import Animal_welfare
import functions
# l is the list corresponding to Dict[phone_num]
# incomingMsg is the incoming_msg


suffix_in_hindi = '\n\nहिंदी में भाषा बदलने के लिए कृपया *hindi* टाइप करें'
suffix_in_english = '\n\nTo change the language in English, please type *English*'
suffix_in_punjabi = '\n\nਭਾਸ਼ਾ ਨੂੰ ਪੰਜਾਬੀ ਵਿੱਚ ਬਦਲਣ ਲਈ *punjabi* ਟਾਈਪ ਕਰੋ'
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
            '*Type 0 for veterinary hotline*\n\n' \
            'Please choose from the following options: \n\n' \
            '*1.* Pet Owner\n' \
            '*2.* Livestock / Poultry Owner\n' \
            '*3.* Para-Veterinarian\n' \
            '*4.* Veterinarian\n' \
            '*5.* Student\n' \
            '*6.* General Services\n'+ suffix_in_hindi+suffix_in_punjabi


        r_hindi = 'अरे! क्या नंदी, मैं आपकी कैसे मदद कर सकता हूँ? क्या मैं पहले जान सकता हूँ कि दूसरी तरफ कौन है?\n\n' \
            '*पशु चिकित्सा हॉटलाइन के लिए 0 टाइप करें*\n\n' \
            'कृपया निम्नलिखित विकल्पों में से चुनें: \n\n' \
            '*1.* पालतू मालिक\n' \
            '*2.* पशुधन / कुक्कुट मालिक\n' \
            '*3.* पैरा-पशु चिकित्सक\n' \
            '*4.* पशु चिकित्सक\n' \
            '*5.* विद्यार्थी\n' \
            '*6.* सामान्य सेवाएं\n' + suffix_in_english+suffix_in_punjabi

        r_punjabi = 'ਸਤ ਸ੍ਰੀ ਅਕਾਲ! ਮੈਂ ਨੰਦੀ ਹਾਂ, ਮੈਂ ਤੁਹਾਡੀ ਕਿਵੇਂ ਮਦਦ ਕਰ ਸਕਦਾ ਹਾਂ? ਕੀ ਮੈਂ ਪਹਿਲਾਂ ਜਾਣ ਸਕਦਾ ਹਾਂ ਕਿ ਦੂਜੇ ਪਾਸੇ ਕੌਣ ਹੈ? \n \n '\
            '*ਵੈਟਰਨਰੀ ਹੌਟਲਾਈਨ ਲਈ 0 ਟਾਈਪ ਕਰੋ*\n \n'\
            'ਕਿਰਪਾ ਕਰਕੇ ਹੇਠ ਲਿਖੇ ਵਿਕਲਪਾਂ ਵਿੱਚੋਂ ਚੁਣੋ: \n \n'\
            '* 1.* ਪਾਲਤੂ ਜਾਨਵਰ ਦਾ ਮਾਲਕ \n'\
            '* 2.* ਪਸ਼ੂਧਨ / ਪੋਲਟਰੀ ਮਾਲਕ \n'\
            '* 3.* ਪੈਰਾ-ਪਸ਼ੂ ਚਿਕਿਤਸਕ \n'\
            '* 4.* ਪਸ਼ੂ ਚਿਕਿਤਸਕ \n'\
            '* 5.* ਵਿਦਿਆਰਥੀ \n'\
            '* 6.* ਆਮ ਸੇਵਾਵਾਂ n' + suffix_in_english+suffix_in_hindi

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

        r_hindi = 'All the above text in hindi' + suffix_hin

    elif l[1:] == ['2']:
        r = 'Which pet do you own ?\n\n' \
            'Please choose from the following options: \n\n' \
            '*1.* Cattle and Buffalo 🐄\n' \
            '*2.* Pig 🐖\n' \
            '*3.* Horse 🐎\n' \
            '*4.* Camel 🐪\n' \
            '*5.* Sheep and Goat 🐑\n' \
            '*6.* Mithun 🐃\n' \
            '*7.* Yak\n' \
            '*8.* Poultry 🐓\n' + suffix_eng

        r_hindi = 'आपके पास कौन सा पालतू जानवर है?\n\n' \
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
            '* 1.* ਗਾਂ ਅਤੇ ਮੱਝ 🐄 \n'\
            '* 2.* ਸੂਰ 🐖 \n'\
            '* 3.* ਘੋੜਾ 🐎 \n'\
            '* 4.* ਊਠ 🐪 \n'\
            '* 5.* ਭੇਡ ਅਤੇ ਬੱਕਰੀ 🐑 \n'\
            '* 6.* ਮਿਥੁਨ 🐃 \n'\
            '* 7.* ਯਾਕ \n'\
            '* 8.* ਪੋਲਟਰੀ 🐓 \n' + suffix_punjabi

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

        r_hindi = 'All the above text in hindi' + suffix_hin


    elif l[1:] == ['6']:
        r = 'Which general service do you want ?\n\n' \
            'Please choose from the following options: \n\n' \
            '*1.* Animal Insurance \n' \
            '*2.* Animal Adoption \n' \
            '*3.* Buy Pet \n' \
            '*4.* Anti-Animal Welfare Reporting \n' \
            '*5.* E-Platform for animal farmers \n' \
            '*6.* Mobile Applications \n' + suffix_eng

        r_hindi = 'All the above text in hindi' + suffix_hin
            

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

        r_hindi = 'All the above text in hindi' + suffix_hin

    elif l[1:] == ['1','2']:
        r = 'What service / info do you want for your Cat? 🐈\n\n' \
            'Please choose from the following options: \n\n' \
            '*1.* Vaccination 💉\n' \
            '*2.* Deworming 💊\n' \
            '*3.* Feed 🍲\n' \
            '*4.* Immunity Boosters 🍶\n' \
            '*5.* Boarding 🏡\n' \
            '*6.* FAQs ❓\n' + suffix_eng

        r_hindi = 'All the above text in hindi' + suffix_hin

    elif l[1:] == ['1','3']:
        r = 'What service / info do you want for your Rabbit? 🐰\n\n' \
            'Please choose from the following options: \n\n' \
            '*1.* Vaccination 💉\n' \
            '*2.* Deworming 💊\n' \
            '*3.* Feed 🍲\n' \
            '*4.* FAQs ❓\n' + suffix_eng

        r_hindi = 'All the above text in hindi' + suffix_hin

    elif l[1:] == ['1','4']:
        r = 'What service / info do you want for your Guinea Pig? 🐭\n\n' \
            'Please choose from the following options: \n\n' \
            '*1.* Feed 🍲\n' \
            '*2.* FAQs ❓\n' + suffix_eng

        r_hindi = 'All the above text in hindi' + suffix_hin

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
            '*2.* कृमिनाशक \n' \
            '*3.* फ़ीड 🍲\n' \
            '*4.* चारा 🍶\n' \
            '*5.* अन्य 🏡\n' \
            '*6.* पशु टैगिंग \n' \
            '*7.* ई टी टी \n' \
            '*8.* लिंग क्रमबद्ध वीर्य \n' \
            '*9.* वीर्य स्टेशन \n' + suffix_hin

        r_punjabi = 'ਤੁਸੀਂ ਆਪਣੇ ਗਾਂ / ਮੱਝ ਲਈ ਕਿਹੜੀ ਸੇਵਾ / ਜਾਣਕਾਰੀ ਚਾਹੁੰਦੇ ਹੋ? \n \n '\
            'ਕਿਰਪਾ ਕਰਕੇ ਹੇਠ ਲਿਖੇ ਵਿਕਲਪਾਂ ਵਿੱਚੋਂ ਚੁਣੋ: \n \n'\
            '* 1.* ਟੀਕਾਕਰਣ  \n'\
            '* 2.* ਕੀਟਾਣੂ ਰਹਿਤ 💊 \n'\
            '* 3.* ਫੀਡ 🍲 \n'\
            '* 4.* ਚਾਰਾ 🍶 \n'\
            '* 5.* ਹੋਰ 🏡 \n'\
            '* 6.* ਪਸ਼ੂ ਟੈਗਿੰਗ  \n'\
            '* 7.* ਈ ਟੀ ਟੀ \n'\
            '* 8.* ਲਿੰਗ ਕ੍ਰਮਬੱਧ ਵੀਰਜ \n'\
            '* 9.* ਵੀਰਜ ਸਟੇਸ਼ਨ \n' + suffix_punjabi

    elif l[1:] == ['2','2']:
        r = 'What service / info do you want for your Pig? 🐖\n\n' \
            'Please choose from the following options: \n\n' \
            '*1.* Vaccination 💉\n' \
            '*2.* Deworming 💊\n' \
            '*3.* Feed 🍲\n' \
            '*4.* Immunity and Health Boosters 🍶\n' + suffix_eng

        r_hindi = 'All the above text in hindi' + suffix_hin

    elif l[1:] == ['2','3']:
        r = 'What service / info do you want for your Horse? 🐎\n\n' \
            'Please choose from the following options: \n\n' \
            '*1.* Vaccination 💉\n' \
            '*2.* Deworming 💊\n' \
            '*3.* Feed 🍲\n' \
            '*4.* Immunity and Health Boosters 🍶\n' + suffix_eng

        r_hindi = 'All the above text in hindi' + suffix_hin

    elif l[1:] == ['2','4']:
        r = 'What service / info do you want for your Camel? 🐪\n\n' \
            'Please choose from the following options: \n\n' \
            '*1.* Vaccination 💉\n' \
            '*2.* Deworming 💊\n' \
            '*3.* Feed 🍲\n' \
            '*4.* Immunity and Health Boosters 🍶\n' + suffix_eng

        r_hindi = 'All the above text in hindi' + suffix_hin

    elif l[1:] == ['2','5']:
        r = 'What service / info do you want for your Sheep and Goat? 🐑\n\n' \
            'Please choose from the following options: \n\n' \
            '*1.* Vaccination 💉\n' \
            '*2.* Deworming 💊\n' \
            '*3.* Feed 🍲\n' \
            '*4.* Immunity and Health Boosters 🍶\n' + suffix_eng

        r_hindi = 'All the above text in hindi' + suffix_hin

    elif l[1:] == ['2','6']:
        r = 'What service / info do you want for your Mithun? 🐃\n\n' \
            'Please choose from the following options: \n\n' \
            '*1.* Vaccination 💉\n' \
            '*2.* Deworming 💊\n' \
            '*3.* Feed 🍲\n' \
            '*4.* Immunity and Health Boosters 🍶\n' + suffix_eng

        r_hindi = 'All the above text in hindi' + suffix_hin

    elif l[1:] == ['2','7']:
        r = 'What service / info do you want for your Yak? \n\n' \
            'Please choose from the following options: \n\n' \
            '*1.* Vaccination 💉\n' \
            '*2.* Deworming 💊\n' \
            '*3.* Feed 🍲\n' \
            '*4.* Immunity and Health Boosters 🍶\n' + suffix_eng

        r_hindi = 'All the above text in hindi' + suffix_hin

    elif l[1:] == ['2','8']:
        r = 'What service / info do you want for your Poultry? 🐓\n\n' \
            'Please choose from the following options: \n\n' \
            '*1.* Vaccination 💉\n' \
            '*2.* Deworming 💊\n' \
            '*3.* Feed 🍲\n' \
            '*4.* Immunity and Health Boosters 🍶\n' + suffix_eng

        r_hindi = 'All the above text in hindi' + suffix_hin

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

        r_hindi = 'All the above text in hindi' + suffix_hin


    elif l[1:] == ['6','5']:
        r = 'What E-Platform do you want to try? \n\n' \
            'Please choose from the following options: \n\n' \
            '*1.* E-Gopala \n' \
            '*2.* Kisan Sarthi \n' \
            '*3.* Kisan Mitr \n' \
            '*4.* Farmer Portal of India \n' \
            '*5.* DAHD \n' + suffix_eng

        r_hindi = 'All the above text in hindi' + suffix_hin

    # -------------------------Animal Welfare----------------------------

    elif l[1:] == ['6','4']:
        r= "*Send us an image depicting Animal abuse/ anti- animal welfare.* \n\n"


        r_hindi = 'All the above text in hindi'

    elif l[1:3] == ['6', '4'] and len(l) == 4:
        r = "*Thanks! Write a short description for the image you sent.*"
        r_hindi = 'All the above text in hindi'
    elif l[1:3] == ['6', '4'] and len(l) == 5:
        r = "Share the exact location of site, or type in exact address of site with pincode."
        r_hindi = 'All the above text in hindi'
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

    elif l[1:] == ['1','1','1']:
        r = 'Here\'s the vaccination chart for your dog ! 🎉\n\n' \
            'Nearest Vaccination Centers - *Feature Coming Soon\n*' + suffix_eng
        r_hindi = 'All the above text in hindi' + suffix_hin
        mediaLink = 'https://firebasestorage.googleapis.com/v0/b/jeevbot.appspot.com/o/dogvcc.jpg?alt=media&token=b2e7e0d5-092f-436c-af20-ee7f0affd90c'
        mediaFlag = 1

    elif l[1:] == ['1','2','1']:
        r = 'Here\'s the vaccination chart for your cat ! 🎉\n\n' \
            'Nearest Vaccination Centers - *Feature Coming Soon\n*' + suffix_eng
        r_hindi = 'All the above text in hindi' + suffix_hin
        mediaLink = 'https://firebasestorage.googleapis.com/v0/b/jeevbot.appspot.com/o/dogvcc.jpg?alt=media&token=b2e7e0d5-092f-436c-af20-ee7f0affd90c'
        mediaFlag = 1

    elif l[1:] == ['1','3','1']:
        r = 'Here\'s the vaccination chart for your Rabbit ! 🎉\n\n' \
            'Nearest Vaccination Centers - *Feature Coming Soon\n*' + suffix_eng
        r_hindi = 'All the above text in hindi' + suffix_hin
        mediaLink = 'https://firebasestorage.googleapis.com/v0/b/jeevbot.appspot.com/o/dogvcc.jpg?alt=media&token=b2e7e0d5-092f-436c-af20-ee7f0affd90c'
        mediaFlag = 1


    elif l[1:-1] == ['4','1']:
        print(l[-1])

        name,registration_number,phone_number,address,city,state,pincode = map(str,l[-1].split('\n'))
        r,r_hindi = Registrations.registerVeterinarian(name,registration_number,phone_number,address,city,state,pincode)

        #     here func will return both r and r_hindi itself. No need to add here




    



    # ----------------- Level 3 - End ---------------------


    else:
        r = 'Give a valid input please! 🥺'
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


