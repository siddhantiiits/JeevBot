import requests
import firebase_admin
import google.cloud
from datetime import date, timedelta , time, datetime

from firebase_admin import credentials, initialize_app, storage, firestore

def registerVeterinarian(name, registrationNumber, phoneNumber, address, city, state, pincode ):

    tomorrow = date.today() + timedelta(days = 1)
    tomorrow = date.today() + timedelta(days=1)
    now = datetime.now()
    current_time = now.strptime("10:30", "%H:%M")
    current_time = current_time.strftime("%I:%M %p")
    registerDate = tomorrow.strftime("%d/%m/%Y")
    # Name
    # Registration Number
    # Phone Number
    # Address
    # City
    # State
    # Pincode

    # Thanks for submission, your registration will be confirmed by { current time + 24 hours }.
    # If you wish to un-register yourself anytime. Mail us at nandi.development@gmail.com
    # res = requests.get(mediaUrl)
    # res = res.content

    cred = credentials.Certificate("nandi-2adc2-firebase-adminsdk-4gdo7-2838d71565.json")
    initialize_app(cred, {'storageBucket': 'nandi-2adc2.appspot.com'})

    # Put your local file path

    # bucket = storage.bucket()
    # blob = bucket.blob(userPhoneNumber+'_'+imageDescription)
    # blob.upload_from_string(res)

    # Opt : if you want to make public access from the URL
    # blob.make_public()
    # link = blob.public_url  #image uploaded to firebase storage and link to image stored in 'link'


    store = firestore.client()

    doc_ref = store.collection(u'Registered Veterinarians')
    doc_ref.add({'Name':name,'Registration Number':registrationNumber,'Phone Number': phoneNumber,'Address':address,
                 'City':city, 'State':state,'Pincode':pincode})

    return 'Thanks for submission, *your registration will be confirmed by ' +registerDate +' '+current_time +'.*\n\n*If you wish to un-register yourself anytime. Mail us at nandi.development@gmail.com*\n\n',"All this text in hindi"



# link = registerVeterinarian(
#     'Sherlock Holmes', 'PCXVT5502X34', '+912837282838', '221 Bakers Street', 'London', 'Royal', '2100182'
# )
# print(link)






