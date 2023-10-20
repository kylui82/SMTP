# SMTP

 Step 1:
- Create a gmail account for testing. 
- Set up two-authentication
- Get the App passwords
<img width="442" alt="image" src="https://github.com/kylui82/TCP-Python/assets/101900083/67be777f-31bc-4c5b-8bf8-f5db80e311f6">


Step 2:
- Open the smtpclientLab4.py in PyCharm
- Change SMTP_USERNAME and SMTP_PASSWORD as your testing gmail address and the app password you get just now.


Step 3:
- Fill in the sender email, receiver email, email subject, cc email

EMAIL_TO = ["testing@gmail.com"] 

EMAIL_FROM = "testing@gmail.com " 

EMAIL_SUBJECT = "Email Subject: "

EMAIL_CC = ['efg@gmail.com', 'abc@gmail.com']


Step 4:
- You can add attachment to the email by placing the file at same directory of the python file. Fill in the filename and file type at below lines:
- filename = "example.txt"
- subtype='txt', filename='example.txt'


Step 5:
- Run the file
- You should receive the email like below one:
<img width="452" alt="image" src="https://github.com/kylui82/SMTP/assets/101900083/047d30e3-704a-43f7-86ac-996944d72fe6">

