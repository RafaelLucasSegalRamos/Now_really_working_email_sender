#! C:\Users\rafae\AppData\Local\Programs\Python\Python310\python.exe

import cgi, os
from fileinput import close
import cgitb
import win32com.client as win32
import smtplib
import email.message
print('content-type:text/html\r\n\r\n')

cgitb.enable()
form = cgi.FieldStorage()
nome = str(form.getvalue("nome"))
Text = str(form.getvalue("texto"))

archive = form["filename"]

filenames = os.path.basename(archive.filename)
open("tem/"+ filenames, "wb").write(archive.file.read())

# print(f"""
#       <!DOCTYPE html>
#         <html lang="pt-br">
#         <head>
#             <meta charset="UTF-8">
#             <meta http-equiv="X-UA-Compatible" content="IE=edge">
#             <meta name="viewport" content="width=device-width, initial-scale=1.0">
#             <title>Teste do texto</title>
#         </head>
#         <body>
#         <h1 style="margin-top: 20px;"> Olá meu nome é {nome} </h1>
#         <img src="tem/{filenames}" alt="N sei pq n funciona" style="margin-top: 40px;">
#         <p style="margin-top: 40px;">{Text}</p>
#         </body>
#         </html>
#       """)

corpo_email = f"""
    <h1> Olá gosta de dizer sobre seu site <h1>
    <img src="tem/{filenames}" alt="N sei pq n funciona" style="margin-top: 40px;">

    <p style="margin-top:30px;"> {Text} </p>
"""

msg = email.message.Message()
msg['Subject'] = f"Olá meu nome é {nome}"
msg['From'] = 'rafael.testescodigos@gmail.com'
msg['To'] = 'mamacosupremo.sol@gmail.com'
password = "I won't show it"
msg.add_header('Content-Type', 'text/html')
msg.set_payload(corpo_email)

s = smtplib.SMTP('smtp.gmail.com: 587')
s.starttls()

s.login(msg['From'], password)
s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
print('Email enviado') 