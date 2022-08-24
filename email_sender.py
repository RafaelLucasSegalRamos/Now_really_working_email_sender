#! C:\Users\rafae\AppData\Local\Programs\Python\Python310\python.exe

import cgi, os
import win32com.client as win32
print('content-type:text/html\r\n\r\n')
outlook = win32.Dispatch('outlook.application')

form =  cgi.FieldStorage()
nome = str(form.getvalue("pname"))
Text = str(form.getvalue("des"))

File = form['filename']

fn = os.path.basename(File.filename)

titulo = f'Ola meu nome é {nome}'

email = outlook.CreateItem(0)


email.To = "mamacosupremo.sol@gmail.com"
email.Subject = titulo
email.HTMLbody = (f"""
                    <h1> Olá Rafael!</h1>
                    
                    <p>{Text}</p>
                    
                    <p> E aqui uma pequena supresa: </p>
                    
                    <a href="{fn}"><img scr="fn"></a>
                    
                    <h2> Obrigado por ter lido minha menssagem</h2>
                    <h1> De: {nome}</h1>
                    """)
email.Send()
print("Email Enviado")   