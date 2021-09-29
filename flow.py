from englisttohindi.englisttohindi import EngtoHindi
# l is the list corresponding to Dict[phone_num]
# incomingMsg is the incoming_msg
def e2h(message):
    res = EngtoHindi(message)
    p = res.convert
    return p

suffix = '\nSelect from the above options by typing number corresponding to the option.\n\nType *home* to go to main menu. \nType *back* to go back to previous menu.'

def process(l,incomingMsg):
    m = ''
    mediaFlag = 0
    # print(l)
    if l == []:
        l.append('hin')
    else:
        l.append(incomingMsg)
    # print(l)

    if incomingMsg == 'home':
        l.clear()
        l.append('hin')
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
            '*6.* General Services\n' \

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
            '*7.* Other Exotic Species \n' \

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
            '*8.* Poultry 🐓\n' \

    elif l[1:] == ['3']:
        r = 'Hey Vet!\nWhat do you want ?\n\n' \
            'Please choose from the following options: \n\n' \
            '*1.* Want to Register yourself \n' \
            '*2.* Want Vaccination and Deworming Handbook \n' \

    elif l[1:] == ['4']:
        r = 'Hey Vet!\nWhat do you want ?\n\n' \
            'Please choose from the following options: \n\n' \
            '*1.* Want to Register yourself \n' \
            '*2.* Want Vaccination and Deworming Handbook \n' \
        
    elif l[1:] == ['5']:
        r = 'Hey Buddy!\nWhat do you want ?\n\n' \
            'Please choose from the following options: \n\n' \
            '*1.* Want Vaccination and Deworming Handbook \n' \


    elif l[1:] == ['6']:
        r = 'Which general service do you want ?\n\n' \
            'Please choose from the following options: \n\n' \
            '*1.* Animal Insurance \n' \
            '*2.* Animal Adoption \n' \
            '*3.* Buy Pet \n' \
            '*4.* Anti-Animal Welfare Reporting \n' \
            '*5.* E-Platform for animal farmers \n' \
            '*6.* Mobile Applications \n' \
            

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
            '*7.* FAQs ❓\n' \

    elif l[1:] == ['1','2']:
        r = 'What service / info do you want for your Cat? 🐈\n\n' \
            'Please choose from the following options: \n\n' \
            '*1.* Vaccination 💉\n' \
            '*2.* Deworming 💊\n' \
            '*3.* Feed 🍲\n' \
            '*4.* Immunity Boosters 🍶\n' \
            '*5.* Boarding 🏡\n' \
            '*6.* FAQs ❓\n' \

    elif l[1:] == ['1','3']:
        r = 'What service / info do you want for your Rabbit? 🐰\n\n' \
            'Please choose from the following options: \n\n' \
            '*1.* Vaccination 💉\n' \
            '*2.* Deworming 💊\n' \
            '*3.* Feed 🍲\n' \
            '*4.* FAQs ❓\n' \

    elif l[1:] == ['1','4']:
        r = 'What service / info do you want for your Guinea Pig? 🐭\n\n' \
            'Please choose from the following options: \n\n' \
            '*1.* Feed 🍲\n' \
            '*2.* FAQs ❓\n' \

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
            '*9.* Semen Stations \n' \

    elif l[1:] == ['2','2']:
        r = 'What service / info do you want for your Pig? 🐖\n\n' \
            'Please choose from the following options: \n\n' \
            '*1.* Vaccination 💉\n' \
            '*2.* Deworming 💊\n' \
            '*3.* Feed 🍲\n' \
            '*4.* Immunity and Health Boosters 🍶\n' \

    elif l[1:] == ['2','3']:
        r = 'What service / info do you want for your Horse? 🐎\n\n' \
            'Please choose from the following options: \n\n' \
            '*1.* Vaccination 💉\n' \
            '*2.* Deworming 💊\n' \
            '*3.* Feed 🍲\n' \
            '*4.* Immunity and Health Boosters 🍶\n' \

    elif l[1:] == ['2','4']:
        r = 'What service / info do you want for your Camel? 🐪\n\n' \
            'Please choose from the following options: \n\n' \
            '*1.* Vaccination 💉\n' \
            '*2.* Deworming 💊\n' \
            '*3.* Feed 🍲\n' \
            '*4.* Immunity and Health Boosters 🍶\n' \

    elif l[1:] == ['2','5']:
        r = 'What service / info do you want for your Sheep and Goat? 🐑\n\n' \
            'Please choose from the following options: \n\n' \
            '*1.* Vaccination 💉\n' \
            '*2.* Deworming 💊\n' \
            '*3.* Feed 🍲\n' \
            '*4.* Immunity and Health Boosters 🍶\n' \

    elif l[1:] == ['2','6']:
        r = 'What service / info do you want for your Mithun? 🐃\n\n' \
            'Please choose from the following options: \n\n' \
            '*1.* Vaccination 💉\n' \
            '*2.* Deworming 💊\n' \
            '*3.* Feed 🍲\n' \
            '*4.* Immunity and Health Boosters 🍶\n' \

    elif l[1:] == ['2','7']:
        r = 'What service / info do you want for your Yak? \n\n' \
            'Please choose from the following options: \n\n' \
            '*1.* Vaccination 💉\n' \
            '*2.* Deworming 💊\n' \
            '*3.* Feed 🍲\n' \
            '*4.* Immunity and Health Boosters 🍶\n' \

    elif l[1:] == ['2','8']:
        r = 'What service / info do you want for your Poultry? 🐓\n\n' \
            'Please choose from the following options: \n\n' \
            '*1.* Vaccination 💉\n' \
            '*2.* Deworming 💊\n' \
            '*3.* Feed 🍲\n' \
            '*4.* Immunity and Health Boosters 🍶\n' \

    elif l[1:] == ['6','5']:
        r = 'What E-Platform do you want to try? \n\n' \
            'Please choose from the following options: \n\n' \
            '*1.* E-Gopala \n' \
            '*2.* Kisan Sarthi \n' \
            '*3.* Kisan Mitr \n' \
            '*4.* Farmer Portal of India \n' \
            '*5.* DAHD \n' \


    # ----------------- Level 2 - End ---------------------


    # ----------------- Level 3 - Begin ---------------------
        # Update their charts location

    elif l[1:] == ['1','1','1']:
        r = 'Here\'s the vaccination chart for your dog ! 🎉\n\n' \
            'Nearest Vaccination Centers - *Feature Coming Soon\n*'
        m = 'https://firebasestorage.googleapis.com/v0/b/jeevbot.appspot.com/o/dogvcc.jpg?alt=media&token=b2e7e0d5-092f-436c-af20-ee7f0affd90c'
        mediaFlag = 1

    elif l[1:] == ['1','2','1']:
        r = 'Here\'s the vaccination chart for your cat ! 🎉\n\n' \
            'Nearest Vaccination Centers - *Feature Coming Soon\n*'
        m = 'https://firebasestorage.googleapis.com/v0/b/jeevbot.appspot.com/o/dogvcc.jpg?alt=media&token=b2e7e0d5-092f-436c-af20-ee7f0affd90c'
        mediaFlag = 1

    elif l[1:] == ['1','3','1']:
        r = 'Here\'s the vaccination chart for your Rabbit ! 🎉\n\n' \
            'Nearest Vaccination Centers - *Feature Coming Soon\n*'
        m = 'https://firebasestorage.googleapis.com/v0/b/jeevbot.appspot.com/o/dogvcc.jpg?alt=media&token=b2e7e0d5-092f-436c-af20-ee7f0affd90c'
        mediaFlag = 1

    



    # ----------------- Level 3 - End ---------------------


    else:
        r = 'Give a valid input please! 🥺'
        l.pop()
        return r,0,''



    r = r+suffix

    # if l[0]=='hin':
    #     r=e2h(r)

    return r,m,mediaFlag



