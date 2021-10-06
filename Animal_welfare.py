import requests
import firebase_admin
import google.cloud
from firebase_admin import credentials, initialize_app, storage, firestore

def animalWelfare(mediaUrl, imageDescription, userPhoneNumber, userName, pincode, location ):
    res = requests.get(mediaUrl)
    res = res.content
    # print(res)

    cred = credentials.Certificate("nandi-2adc2-firebase-adminsdk-4gdo7-2838d71565.json")
    if not firebase_admin._apps:
        initialize_app(cred, {'storageBucket': 'nandi-2adc2.appspot.com'})

    # Put your local file path

    bucket = storage.bucket()
    blob = bucket.blob(userPhoneNumber+'_'+imageDescription)
    blob.upload_from_string(res)


    # Opt : if you want to make public access from the URL
    blob.make_public()
    link = blob.public_url  #image uploaded to firebase storage and link to image stored in 'link'


    store = firestore.client()

    doc_ref = store.collection(u'AnimalWelfare')
    doc_ref.add({'Name':userName,'User Phone Number':userPhoneNumber,'Image URL': link,'Image Description':imageDescription ,
                 'Pincode':pincode, 'Location X-Coordinate':location[0],'Location Y-Coordinate':location[1]})

    return 'Thanks for sharing with us, we are working on the same and trying to help ASAP. The Image you uploaded is available at: '+blob.public_url + '\n\n'



# link = animalWelfare('https://storage.googleapis.com/nandi-2adc2.appspot.com/12345_A%20dog%20sneaking.jpg',"A dog sneaking","12345","SiddhantT","243006",("2.33","4.6"))
# print(link)






