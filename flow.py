import requests
import os
import Registrations
import Animal_welfare
# l is the list corresponding to Dict[phone_num]
# incomingMsg is the incoming_msg



suffix = '\nSelect from the above options by typing number corresponding to the option.\n\nType *home* to go to main menu. \nType *back* to go back to previous menu.'

def process(l,incomingMsg,mediaurl,phonenum):
    mediaLink = ''
    mediaFlag = 0
    # print(l)
    if incomingMsg:
        if l == []:
            l.append('hin')
        else:
            l.append(incomingMsg)
    else:
        if mediaurl:
            l.append(mediaurl)
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
            '*123456*\n\n' \


    elif l[1:] == ['6','5']:
        r = 'What E-Platform do you want to try? \n\n' \
            'Please choose from the following options: \n\n' \
            '*1.* E-Gopala \n' \
            '*2.* Kisan Sarthi \n' \
            '*3.* Kisan Mitr \n' \
            '*4.* Farmer Portal of India \n' \
            '*5.* DAHD \n' \

    elif l[1:] == ['6','4']:
        r= "Send us an image depicting Animal abuse/ anti- animal welfare. \n\n"
    elif l[1:3] == ['6', '4'] and len(l) == 4:
        r = "Thanks! Write a short description for the image you sent."
    elif l[1:3] == ['6', '4'] and len(l) == 5:
        r = "Share the exact location of site, or type in exact address of site with pincode."
    elif l[1:3] == ['6', '4'] and len(l) == 6:
        r = Animal_welfare.animalWelfare(l[3],l[4],phonenum,'Test XYZ',l[5])




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
            'Nearest Vaccination Centers - *Feature Coming Soon\n*'
        mediaLink = 'https://firebasestorage.googleapis.com/v0/b/jeevbot.appspot.com/o/dogvcc.jpg?alt=media&token=b2e7e0d5-092f-436c-af20-ee7f0affd90c'
        mediaFlag = 1

    elif l[1:] == ['1','2','1']:
        r = 'Here\'s the vaccination chart for your cat ! 🎉\n\n' \
            'Nearest Vaccination Centers - *Feature Coming Soon\n*'
        mediaLink = 'https://firebasestorage.googleapis.com/v0/b/jeevbot.appspot.com/o/dogvcc.jpg?alt=media&token=b2e7e0d5-092f-436c-af20-ee7f0affd90c'
        mediaFlag = 1

    elif l[1:] == ['1','3','1']:
        r = 'Here\'s the vaccination chart for your Rabbit ! 🎉\n\n' \
            'Nearest Vaccination Centers - *Feature Coming Soon\n*'
        mediaLink = 'https://firebasestorage.googleapis.com/v0/b/jeevbot.appspot.com/o/dogvcc.jpg?alt=media&token=b2e7e0d5-092f-436c-af20-ee7f0affd90c'
        mediaFlag = 1

    elif l[1:-1] == ['4','1']:
        print(l[-1])

        name,registration_number,phone_number,address,city,state,pincode = map(str,l[-1].split('\n'))
        r = Registrations.registerVeterinarian(name,registration_number,phone_number,address,city,state,pincode)



    



    # ----------------- Level 3 - End ---------------------


    else:
        r = 'Give a valid input please! 🥺'
        l.pop()
        return r,'',0



    r = r+suffix

    # if l[0]=='hin':
    #     r=e2h(r)

    return r,mediaLink,mediaFlag


