print("ping con ---> ping3")

import os #CON ESTO HACEMOS COMANDOS COMO LA TERMINAL
print("Introduzca una red")

red=input("Red: ")

ping = os.system("ping -n 1 " + red)
if rep == 0:
	print("OK")
else:
	print("No responde")

