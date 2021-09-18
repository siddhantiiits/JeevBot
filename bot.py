from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse




app = Flask(__name__)
#
l=[]
Dict={}
@app.route('/bot', methods=['POST'])
def bot():

    incoming_msg = request.values.get('Body','').lower()
    phone_num = request.values.get('From','').lower()
    if phone_num in Dict:
        print("Already in dict")
    else:
        Dict[phone_num]=[]

    resp = MessagingResponse()

    msg = resp.message()

    if incoming_msg in ('home' , 'hi'):
        Dict[phone_num].clear()
        r = 'Hey! How can I help you today ? \n1) Help \n2) Vet Call'


    # if not Dict[phone_num] and incoming_msg:
    #     r = 'Hey! How can I help you today ? \n1) Help \n2) Vet Call'

    if len(Dict[phone_num]) == 1 :
        if incoming_msg == '1':
            r = 'What kind of help do you want ?\n*1)* General Help \n*2)* Disease Related Help '
        elif incoming_msg =='2':
            r = 'Please Enter your pincode '
    elif len(Dict[phone_num])==2:
        print(l)
        if Dict[phone_num][1] =='1' and incoming_msg=='1':
            r = 'Help is on the way'
        elif Dict[phone_num][1] =='1' and incoming_msg=='2':
            r = "Disease help is on the way"
        elif Dict[phone_num][1] == '2':
            r = 'Thanks we have recieved your pincode:' + incoming_msg
    else:
        r = 'Give a valid input please! 🥺'




    msg.body(r)
    # msg.media('https://user-images.githubusercontent.com/34777376/77290801-f2421280-6d02-11ea-8b08-fdb516af3d5a.jpeg')
    if incoming_msg:
        Dict[phone_num].append(incoming_msg)

    return str(resp)


if __name__ == '__main__':
    app.run(debug=True)
