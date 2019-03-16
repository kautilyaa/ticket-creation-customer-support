from category import *
from subject_detection import *
from send_email import *
from feature_extraction import *
import easyimap
import time

tickets = []
token_id = 10000

def extract_and_store_info(email, ticket):
    result = {}
    if not('category' in ticket.keys()):
        ticket['category'] = category_classifier.classify(categorize_feature(email))
        ticket['subject'] = subject_classifier.classify(subject_feature(email))
    result['content'] = email
    if (not ticket['features']):
        ticket['features'] = {}
    if (not ticket['response_list']):
        ticket['response_list'] = []
    try:
        ticket['required_details'] = requirements[ticket['subject']]
    except:
        ticket['required_details'] = []
    
    # EXTRACTING DETAILS
    for (x) in ticket['required_details']:
        if (len(x) > 1):
            feature = extract_feature(email['body'], x[0], x[1])
        else:
            feature = extract_feature(email['body'], x[0])
        if (feature):
            ticket['features'][x[0][0]] = feature

    #if (ticket['status'] == 1):
        

    ticket['status'] = 1 # INFORMATION PENDING FROM CUSTOMER SIDE
    if (len(ticket['required_details']) == len(ticket['features'])):
        ticket['status'] = 2 # COMPLETE INFORMATION RECEIVED ( PROCEEDED FOR HUMAN SUPPORT )
    

    ticket['response_list'].append(result)

    print(ticket['token_id'])
    print(ticket['category'], " : ", ticket['subject'])
    
    return result

while(1):
    time.sleep(3)
    imapper = easyimap.connect('imap.gmail.com','USERNAME@gmail.com', 'PASSWORD')
    mail_list = imapper.unseen(2)
    if (not mail_list):
        continue
	
    for mail_id in imapper.listids(limit=1):
        print("Found Mail")
        mail = imapper.mail(mail_id)

        mail_id = mail.from_addr
        mail_content = {'subject': mail.title, 'body':mail.body}

        ticket = {}
        
        for t in tickets:
            if (mail_id == t['mail']):
                ticket = t
                break

        if (not ticket):
            token_id += 1
            ticket['status'] = 0
            ticket['token_id'] = token_id
            ticket['mail'] = mail_id
            ticket['features'] = {}
            ticket['response_list'] = []
            try:
                ticket['required_details'] = requirements[ticket['subject']]
            except:
                ticket['required_details'] = []
            tickets.append(ticket)

        extract_and_store_info(mail_content, ticket)
        send_mail(mail_id, ticket)
