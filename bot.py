from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse

conversation = ['Hey! How can I help you today ? \n1) Help \n2) Vet Call'
    ,['What kind of help do you want ?\n*1)* General Help \n*2)* Disease Related Help ',['Help is on the way'],["Disease help is on the way"]]
    ,['Please Enter your pincode ',['Thanks we have recieved your pincode:']]]


welcomemsg01='Hey! How can I help you today ? \n1) Help \n2) Vet Call'
welcomemsg11='What kind of help do you want ?\n*1)* General Help \n*2)* Disease Related Help '
welcomemsg12='Please Enter your pincode '
welcomemsg21='Help is on the way'
welcomemsg22='Disease help is on the way'

listt = [welcomemsg01,
            [welcomemsg11,
                [welcomemsg21
                ]
                [welcomemsg22
                ]
            ]
            [welcomemsg12,
                [
                ]
            ]
        ]

def func(s):
    if(len(s)==6):
        return int(s)
    elif(len(s)!=1):
        return -1
    elif(s[0]=='1'):
        return 1
    elif(s[0]=='2'):
        return 2



app = Flask(__name__)
#
l=[]
Dict={}
stream=listt
@app.route('/bot', methods=['POST'])
def bot():

    incoming_msg = request.values.get('Body','').lower()
    phone_num = request.values.get('From','').lower()
    if phone_num in Dict:
        print("Already in dict")
    else:
        Dict[phone_num]=listt

    resp = MessagingResponse()

    msg = resp.message()

    

    int i = func(incoming_msg)
    if(i==-1):
        if incoming_msg in ('home' , 'hi'):
            r=Dict[phone_num][0]
    elif(len(i)==1):
        Dict[phone_num]=Dict[phone_num][i]
        r=Dict[phone_num][0]


    # if incoming_msg in ('home' , 'hi'):
    #     Dict[phone_num].clear()
    #     r = 'Hey! How can I help you today ? \n1) Help \n2) Vet Call'


    # # if not Dict[phone_num] and incoming_msg:
    # #     r = 'Hey! How can I help you today ? \n1) Help \n2) Vet Call'

    # elif len(Dict[phone_num]) == 1 :
    #     if incoming_msg == '1':
    #         r = 'What kind of help do you want ?\n*1)* General Help \n*2)* Disease Related Help '
    #     elif incoming_msg =='2':
    #         r = 'Please Enter your pincode '
    # elif len(Dict[phone_num])==2:
    #     print(l)
    #     if Dict[phone_num][1] =='1' and incoming_msg=='1':
    #         r = 'Help is on the way'
    #     elif Dict[phone_num][1] =='1' and incoming_msg=='2':
    #         r = "Disease help is on the way"
    #     elif Dict[phone_num][1] == '2':
    #         r = 'Thanks we have recieved your pincode:' + incoming_msg
    else:
        r = 'Give a valid input please! 🥺'




    msg.body(r)
    # msg.media('https://user-images.githubusercontent.com/34777376/77290801-f2421280-6d02-11ea-8b08-fdb516af3d5a.jpeg')
    # if incoming_msg:
    #     Dict[phone_num].append(incoming_msg)


    return str(resp)


if __name__ == '__main__':
    app.run(debug=True)
