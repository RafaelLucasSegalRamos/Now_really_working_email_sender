#! C:\Users\rafae\AppData\Local\Programs\Python\Python310\python.exe

import cgi, os
from ctypes import addressof
import cgitb
import win32com.client as win32
print('content-type:text/html\r\n\r\n')
outlook = win32.Dispatch('outlook.application')


cgitb.enable( )
form =  cgi.FieldStorage()
nome = str(form.getvalue("pname"))
Text = str(form.getvalue("text"))

file = form["filename"]

filenames = os.path.basename(file.filename)
open("C:/xampp/htdocs/Now_really_working_email_sender/tem/"+ filenames, "wb").write(file.file.read())

email = outlook.CreateItem(0)

email.To = "mamacosupremo.sol@gmail.com"
email.Subject = f"Olá meu nome é {nome}"
email.HTMLbody = (f"""
                    <h1 style="background: #222; padding: 20px; border-radius: 20px;"> Olá Rafael!</h1>
                    
                    <p>{Text}</p>
                    
                    <h2> De: </h2> <h1>{nome}</h1>
                    """)
email.Send()
print("Email Enviado")
