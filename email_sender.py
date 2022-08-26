#! C:\Users\rafae\AppData\Local\Programs\Python\Python310\python.exe

import cgi, os
import cgitb
import win32com.client as win32
print('content-type:text/html\r\n\r\n')

cgitb.enable()
outlook = win32.Dispatch('outlook.application')
form =  cgi.FieldStorage()
nome = str(form.getvalue("nome"))
Text = str(form.getvalue("texto"))

file = form["filename"]

filenames = os.path.basename(file.filename)
open("tem/"+ filenames, "wb").write(file.file.read())

print(f"""
      <!DOCTYPE html>
        <html lang="pt-br">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link rel="stylesheet" href="CSS/style.css">
            <title>Teste do texto</title>
        </head>
        <body>
        <h1> Olá meu nome é {nome} </h1>
        <img scr="tem/{filenames}"
        <p>{Text}</p>
        </body>
        </html>
      """)
# email = outlook.CreateItem(0)

# email.To = "mamacosupremo.sol@gmail.com"
# email.Subject = f"Olá meu nome é {nome}"
# email.HTMLbody = (f"""
#                     <h1> Olá Rafael!</h1>
                    
#                     <p>{Text}</p>
#                     <img scr='tem/{filenames}'>
#                     <h2> De: </h2> <h1>{nome}</h1>
#                     """)
# email.Send()