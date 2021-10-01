import requests
from firebase_admin import credentials, initialize_app, storage

def uploadUserImage(mediaUrl, imageDescription, userPhoneNumber, userName, pincode, location ):
    res = requests.get(mediaUrl)
    res = res.content

    cred = credentials.Certificate("nandi-2adc2-4fee8e04fda2.json")
    initialize_app(cred, {'storageBucket': 'nandi-2adc2.appspot.com'})

    # Put your local file path

    bucket = storage.bucket()
    blob = bucket.blob(userPhoneNumber+'_'+imageDescription)
    blob.upload_from_string(res)

    # Opt : if you want to make public access from the URL
    blob.make_public()

    return blob.public_url



link = uploadUserImage('https://storage.googleapis.com/nandi-2adc2.appspot.com/12345_A%20dog%20sneaking.jpg',"A dog sneaking","12345","SiddhantT","243006",("2.33","4.6"))
print(link)




