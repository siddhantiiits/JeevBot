import requests
import firebase_admin
import google.cloud
import urllib



from firebase_admin import credentials, initialize_app, storage, firestore

def animalWelfare(mediaUrl, imageDescription, userPhoneNumber, userName, address, location ):
    print(mediaUrl)
    # headers = {'Content-type': 'content_type_value'}

    req = urllib.request.Request(mediaUrl, method='HEAD', headers={'User-Agent': 'Mozilla/5.0'})
    r = urllib.request.urlopen(req)
    h = r.getheader('Content-Type')
    # print(h)
    type = h.split('/')
    content_ext = type[1]
    content_type = type[0]
    res = requests.get(mediaUrl)
    # print(res)
    res = res.content
    # print(res)

    # print(res)

    cred = credentials.Certificate("nandi-2adc2-firebase-adminsdk-4gdo7-2838d71565.json")
    if not firebase_admin._apps:
        initialize_app(cred, {'storageBucket': 'nandi-2adc2.appspot.com'})

    # Put your local file path



    bucket = storage.bucket()
    blob = bucket.blob(userPhoneNumber+'_'+imageDescription+'.'+content_ext)
    blob.upload_from_string(res)

    print(content_ext)


    # Opt : if you want to make public access from the URL
    blob.make_public()
    link = blob.public_url #image uploaded to firebase storage and link to image stored in 'link'
    print(link)


    store = firestore.client()

    doc_ref = store.collection(u'AnimalWelfare')
    doc_ref.add({'Name':userName,'User Phone Number':userPhoneNumber,'Image URL': link,'Image Description':imageDescription ,
                 'Location':pincode, 'Location X-Coordinate':location[0],'Location Y-Coordinate':location[1],'status':'Not seen yet','finalStatus':'active','remarks':'NA'})

    return 'Thanks for sharing with us, we are working on the same and trying to help ASAP. The '+content_type+' you uploaded is available at: '+blob.public_url + '\n\n', 'हमारे साथ साझा करने के लिए धन्यवाद, हम इस पर काम कर रहे हैं और त्वरित मदद करने की कोशिश कर रहे हैं। आपके द्वारा अपलोड किया गया चित्र/वीडियो यहां उपलब्ध है:'+blob.public_url + '\n\n'



# link = animalWelfare('https://storage.googleapis.com/nandi-2adc2.appspot.com/12345_A%20dog%20sneaking.jpg',"A dog sneaking","12345","SiddhantT","243006",("2.33","4.6"))
# print(link)






