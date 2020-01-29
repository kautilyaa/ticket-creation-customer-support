import imaplib

imap_ssl_host = 'imap.gmail.com'  # imap.mail.yahoo.com
imap_ssl_port = 993
username = Username
password = Password

imap = imaplib.IMAP4_SSL(imap_ssl_host, imap_ssl_port)
imap.login(username, password)

imap.select('Inbox')

tmp, data = imap.search(None, 'ALL')
for num in data[0].split():
	tmp, data = imap.fetch(num, '(RFC822)')
	print('Message: {0}\n'.format(num))
	print(data[0][1])
	break
imap.close()
