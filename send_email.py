import smtplib
from email.message import EmailMessage

requirements = {'Baggage Related': [(['pnr'], r"(\d[\- ]?){10}"), (['bag color', 'color'],)], 'Refund': [(['pnr'] ,r"(\d[\- ]?){10}"), (['train name', 'train'],), (['origin', 'from'],), (['destination', 'to'],), (['mobile no','mobile number','mobile','phone'],r"[+]?(\d[\- ]?){10,13}"), (['card no', 'card number', 'card'], r"(\d[\- ]?)+"), (['booking id', 'transaction id', 'referance id', 'referance no'],), (['refund amount', 'amount'],)], 'Special Assistance': [ (['pnr'], r"(\d[\- ]?){10}"), (['destination', 'to'],), (['origin', 'from'],)]}


def send_mail(mail, ticket):
    sender = 'support@bookticket.com'
    receivers = [mail]

    msg = EmailMessage()
    msg.set_content(generate_mail(ticket))

    msg['Subject'] = "RE: " + ticket['response_list'][0]['content']['subject']
    

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login("USERNAME@gmail.com", "PASSWORD")
    server.sendmail(sender, receivers, msg.as_string())
    server.quit()
    
def generate_mail(ticket):
    cat_info = "\n\nToken ID: {0}\nCATEGORY: {1}\nSUBJECT: {2}".format(ticket['token_id'], ticket['category'], ticket['subject'])
    str1 = "We have received your mail\nIt will be processed shortly.\n"
    if (ticket['status'] == 1):
        str1 = "We have received your mail but it seems some details are missing or wrong.\nPlease send those details.\n"
        for r_feat in ticket['required_details']:
            if not(r_feat[0][0] in ticket['features'].keys()):
                if (r_feat[0][0] == 'pnr'):
                    str1 += "\n" + r_feat[0][0].upper()
                else:
                    str1 += "\n" + r_feat[0][0].title()
    elif (ticket['category'] == 'Appreciation'):
        str1 = "We are glad to hear you liked our services and we hope that you will recommend us to your family and friends"
    elif (ticket['category'] == 'Suggestion'):
        str1 = "Thank you for your suggestion, we appreciate your effort and will try to implement in the best way possible"
    return str1 + cat_info + "\nCheers"
