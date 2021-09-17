from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse





app = Flask(__name__)
#
l=[]
@app.route('/bot', methods=['POST'])
def bot():

    incoming_msg = request.values.get('Body','').lower()
    resp = MessagingResponse()

    msg = resp.message()

    if incoming_msg in ('home' , 'hi'):
        l.clear()


    if not l and incoming_msg:
        r = 'Hey! How can I help you today ? \n1) Help \n2) Vet Call'

    if len(l) == 1 :
        if incoming_msg == '1':
            r = 'What kind of help do you want ?\n1) General Help \n2) Disease Related Help '
        elif incoming_msg =='2':
            r = 'Please Enter your pincode '
    if len(l)==2:
        print(l)
        if l[1] =='1':
            if incoming_msg == '1':
                r = 'Help is on the way'

            elif incoming_msg =='2':
                r = "Disease help is on the way"
        if l[1] == '2':
            r = 'Thanks we have recieved your pincode:' + incoming_msg




    msg.body(r)
    # msg.media('https://user-images.githubusercontent.com/34777376/77290801-f2421280-6d02-11ea-8b08-fdb516af3d5a.jpeg')
    if incoming_msg:
        l.append(incoming_msg)

    return str(resp)


if __name__ == '__main__':
    app.run(debug=True)
