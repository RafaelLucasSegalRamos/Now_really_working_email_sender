#! C:\Users\rafae\AppData\Local\Programs\Python\Python310\python.exe

import cgi, os
import cgitb
import win32com.client as win32
print('content-type:text/html\r\n\r\n')
outlook = win32.Dispatch('outlook.application')
email = outlook.CreateItem(0)

cgitb.enable()
form =  cgi.FieldStorage()
nome = str(form.getvalue("pname"))
Text = str(form.getvalue("text"))

file = form["filename"]

filenames = os.path.basename(file.filename)
open("C:/xampp/htdocs/Now_really_working_email_sender/tem/"+ filenames, "wb").write(file.file.read())

titulo = f"Olá meu nome é {nome}"


email.To = "mamacosupremo.sol@gmail.com"
email.Subject = titulo
email.HTMLbody = (f"""
                    <h1> Olá Rafael!</h1>
                    
                    <p>{Text}</p>
                    <img scr='tem/{filenames}'>
                    <h2> De: </h2> <h1>{nome}</h1>
                    """)
email.Send()