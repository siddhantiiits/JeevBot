import requests
import firebase_admin
import google.cloud


from firebase_admin import credentials, initialize_app, storage, firestore

# def registerVeterinarian(who, name, registrationNumber, phoneNumber, address, city, state, pincode):


def nearestVet(pincode):

    cred = credentials.Certificate("nandi-2adc2-firebase-adminsdk-4gdo7-2838d71565.json")
    if not firebase_admin._apps:
        firebase_admin.initialize_app(cred)

    db = firestore.client()
    leftRange = pincode[:3] + '000'
    rightRange = str(int(pincode[:3])+1) +'000'
    # print(leftRange,rightRange)

    # Note: Use of CollectionRef stream() is prefered to get()
    docs = db.collection(u'Registered Veterinarians').where(u'pincode', u'>=', leftRange).where(u'pincode', u'<', rightRange).stream()

    result = []

    for doc in docs:
        docDict = doc.to_dict()
        result.append([docDict['name'],docDict['phone'],docDict['address'],docDict['city'],docDict['state'],docDict['pincode']])

        # print(f'{doc.id} => {doc.to_dict()}')
    # print(result)
    front = []
    back = []
    for x in range(len(result)):
        if result[x][-1] == pincode:
            front.append(result[x])
        else:
            back.append(result[x])
    result = front + back

    # print(result)
    resultPrefix = 'Thanks for sharing the information, here are the list of veterinarians nearest to you!\n\n'
    resultSuffix = 'Hope this helps! Thankyou 😊'
    resultString = ''
    if not result:
        for x in range(5):

            resultString += 'Mr. Test Vet\n' \
                            '+91 0123456789\n' \
                            '192, Vikas nagar\n' + pincode + '\n'

            resultString += '\'https://www.google.com/maps/search/' + 'test_location\''
            resultString += '\n\n'
    else:
        for x in result:
            resultString += x[0] + '\n' + x[1] + '\n' + x[2] + '\n' + x[3] + '\n' + x[4] +'\n' + x[5] + '\n'
            mapLink = 'https://www.google.com/maps/search/' + x[2] + x[3] + x[4] + x[5]

            resultString += mapLink.replace(" ","_")
            resultString += '\n\n'





    resultString = resultPrefix + resultString + resultSuffix
    return resultString

# print(nearestVet("243006"))