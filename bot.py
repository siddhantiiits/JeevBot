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



    incoming_msg = request.values.get('Body','').lower()
    phone_num = request.values.get('From','').lower()
    if phone_num in Dict:
        print("Already in dict")
    else:
        Dict[phone_num]=[]

    resp = MessagingResponse()
    msg = resp.message()

    print(incoming_msg)
    print(Dict)

    if incoming_msg == 'cleardump':
        r = emptyDictFile()
        msg.body(r)
        return str(resp)



    # print(Dict[phone_num])

    r,m,mediaFlag = process(Dict[phone_num],incoming_msg)
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
