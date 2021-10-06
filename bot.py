from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse
import pickle
from flow import process
from varDump import emptyDictFile



app = Flask(__name__)
#
# l=[]
# Dict={}

@app.route('/bot', methods=['POST'])
def bot():

    # Open the file in binary mode
    with open('file.pkl', 'rb') as file:
        # Call load method to deserialze
        Dict = pickle.load(file)


    print(request)
    print("----")
    print(request.values)
    incoming_msg = request.values.get('Body','').lower()
    phone_num = request.values.get('From','').lower()
    userName = request.values.get('ProfileName','').lower()
    media_url = request.form.get('MediaUrl0')
    if phone_num in Dict:
        print("Already in dict")
    else:
        Dict[phone_num]=[]

    resp = MessagingResponse()
    msg = resp.message()

    print(incoming_msg)
    print(Dict)

    # if media_url:
    #     r = requests.get(media_url)
    #     content_type = r.headers['Content-Type']
    #     username = sender.split(':')[1]  # remove the whatsapp: prefix from the number
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
    #             f.write(r.content)
    #         return respond('Thank you! Your image was received.')
    #     else:
    #         return respond('The file that you submitted is not a supported image type.')
    # else:
    #     return respond('Please send an image!')

    if incoming_msg == 'cleardump':
        r = emptyDictFile()
        msg.body(r)
        return str(resp)



    # print(Dict[phone_num])

    r,m,mediaFlag = process(Dict[phone_num],incoming_msg,media_url,phone_num,userName)
    # print(Dict[phone_num])
    if mediaFlag==0:
        msg.body(r)

    else:
        msg.body(r)
        msg.media(m)


    with open('file.pkl', 'wb') as file:
        # A new file will be created
        pickle.dump(Dict, file)
        print("Dumped")
        print(Dict)



    return str(resp)


if __name__ == '__main__':
    app.run(debug=True)



