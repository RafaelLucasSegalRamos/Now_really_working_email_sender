#! C:\Users\rafae\AppData\Local\Programs\Python\Python310\python.exe

import cgi, os

print('content-type:text/html\r\n\r\n')

form =  cgi.FieldStorage()
nome = str(form.getvalue("pname"))
Text = str(form.getvalue("des"))

File = form['filename']

fn = os.path.basename(File.filename)
open("C:/xampp/htdocs/Now_really_working_email_sender/tem/"+fn, "wb").write(File.file.read())

print("""<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Email sender</title>
</head>
<body>"""
)
print("""<h1> New Message \n(%s)</h1>"""%nome)

print("""<img scr="tem/%s">"""%fn)
print("<h2>%s</h2>"%Text)      

print("""
      </body>
</html> 
""")      


