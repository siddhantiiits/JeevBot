# l is the list corresponding to Dict[phone_num]
# incomingMsg is the incoming_msg

suffix = '\nSelect from the above options by typing number corresponding to the option.\n\nType *home* to go to main menu. \nType *back* to go back to previous menu.'

def process(l,incomingMsg):
    m = ''
    # print(l)
    l.append(incomingMsg)
    # print(l)

    if incomingMsg == 'home':
        l.clear()
        l.append('hi')
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

    # ----------------- Level 2 - End ---------------------


    # ----------------- Level 3 - Begin ---------------------

    elif l[1:] == ['1','1','1']:
        r = 'Here\'s the vaccination chart for your dog ! 🎉\n\n' \
            'Nearest Vaccination Centers - *Feature Comint Soon*'
        m = 'https://firebasestorage.googleapis.com/v0/b/jeevbot.appspot.com/o/dogvcc.jpg?alt=media&token=b2e7e0d5-092f-436c-af20-ee7f0affd90c'



    # ----------------- Level 3 - End ---------------------


    else:
        r = 'Give a valid input please! 🥺'
        l.pop()
        return r



    r = r+suffix
    return r,m



