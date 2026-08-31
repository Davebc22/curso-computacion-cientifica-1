"""
# 8. Realiza un algoritmo que valide si un email es valido
### El texto debe tener un nombre de usuario sin caracteres especiales, el símbolo @, un dominio y una extensión como .com


"""
import re

email =  "allstars!$@gmail.com"

patron = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

if re.match(patron, email):
    print('Correo Válido')
else:
    print('Correo No Válido')
