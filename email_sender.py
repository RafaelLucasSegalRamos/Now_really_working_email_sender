#! C:\Users\rafae\AppData\Local\Programs\Python\Python310\python.exe

import cgi, os
import cgitb
import win32com.client as win32
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
#         <img src="tem/MEIO.jpg" alt="N sei pq n funciona" style="margin-top: 40px;">
#         <p style="margin-top: 40px;">{Text}</p>
#         </body>
#         </html>
#       """)

outlook = win32.Dispatch('outlook.application')
titulo = 'Nova menssagem sobre seu Site!'
menssagem = "só trocando a menssagem msm"
nome = "rafael"

a_email = outlook.CreateItem(0)

a_email.To = "mamacosupremo.sol@gmail.com"
a_email.Subject = titulo
a_email.HTMLbody = (f"""
                    <h1> Olá Rafael!</h1>
                    
                    <p>{menssagem}</p>
                    
                    <h2> De: </h2> <h1>{nome}</h1>
                    """)
a_email.Send()