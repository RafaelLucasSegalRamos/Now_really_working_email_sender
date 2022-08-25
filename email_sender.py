#! C:\Users\rafae\AppData\Local\Programs\Python\Python310\python.exe

import cgi, os
import win32com.client as win32
print('content-type:text/html\r\n\r\n')
outlook = win32.Dispatch('outlook.application')

form =  cgi.FieldStorage()
nome = str(form.getvalue("Nome"))
Text = str(form.getvalue("text"))

File = form['arquivo']

fn = os.path.basename(File.filename)

titulo = f'Ola meu nome é {nome}'

# email = outlook.CreateItem(0)


print("<html><head><title>Titulo1</title></head>")
print(f"<body><h1>{nome}</h1>")
print(f"<img scr='{fn}'>")
print(f"<p>{Text}</p>")
print("</body></html>")
