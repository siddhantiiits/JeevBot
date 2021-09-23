# l is the list corresponding to Dict[phone_num]
# incomingMsg is the incoming_msg
def process(l,incomingMsg):
    # print(l)
    l.append(incomingMsg)
    # print(l)

    if incomingMsg == 'home':
        l.clear()
        l.append('hi')
    elif len(l) > 2 and incomingMsg == 'back':
        l.pop()
        l.pop()
    elif len(l) == 2 and incomingMsg == 'back':
        l.pop()



    if len(l) == 1:
        r = 'Hey! How can I help you today ? \n1) Help \n2) Vet Call'
    elif l[1:] == ['1']:
        r = 'What kind of help do you want ?\n*1)* General Help \n*2)* Disease Related Help '
    elif l[1:] == ['2']:
        r = 'Please Enter your pincode '
    elif l[1:] == ['1','1']:
        r = 'Help is on the way'
    elif l[1:] == ['1','2']:
        r = "Disease help is on the way"
    elif l[1] == '2' and l[2]:
        r = 'Thanks we have recieved your pincode: ' + l[2]
    else:
        r = 'Give a valid input please! 🥺'
        l.pop()

    return r



