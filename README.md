# Ticket Creation Customer Support | Smart India Hackathon Winning solution 2019
For problem statement RV5 : Developing a customer support system for customer communating through email
Automatic ticket creation for Customer Support.<br>
Run email_full.py to start fetching mail from the server and start generating ticket.<br>
## Our topic focus on basically these particular areas:
- The correctness of the data given to the machine by the end user if the format is in the required order with no problems in it then it - proceeds to the step where the final ticket is being sent else it goes to the next step.
- Also to check if the details given by the user are not incomplete. If no the proceed skipping the next steps.
- If  an error in the given input is detected then it will use the Machine language technique(explained in later slide),or will send back the form to the end user.
- The form sent will not loose its existing data, it will only require required missing data.
- Ticket Generation ticket gets generated with all the required details in a given format and gets sent to the user’s email id.

#### For reference refer refer the video in the [link](https://www.youtube.com/watch?v=oH-CcEjNNjs&feature=youtu.be) .<br>
<br>

## Technology Stack

Here the language used is python with pakages like csv, imaplib, smtplib, email, matplotlib, random, re and the most used package is **_nltk_**. For processing the details, it is used to take out the word. 
<br>
## Use Case
![case](https://user-images.githubusercontent.com/36475185/57319808-13196d80-711b-11e9-9d31-6f158c9e1ca5.png)

## Team ✨ :  [Solvers_VIT](https://www.sih.gov.in/pdf/past_events/software_2019.pdf)

* Amul Choudhary<br>
* Anmol Rao<br>
* Shikar Bhardwaj <br>
* Rohan Vashisth<br>
* Panna Nagpal <br>
* Arunbh Yashaswi (Team Leader)<br>


## Instruction 
For running the code please update **get_email.py** before :<br>
```
imap_ssl_host = 'imap.gmail.com'  // imap.mail.yahoo.com
imap_ssl_port = 993  //select the port
username = 'username@gmail.com'//put your username here
password = 'PASSWORD'// put the password here
  ```
