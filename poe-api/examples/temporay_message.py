import poe
import logging
import sys

#send a message and immediately delete it

token = "DAsBbOza4ZFMb1vJYj6Vfg%3D%3D"
poe.logger.setLevel(logging.INFO)
client = poe.Client(token)


message = sys.argv[1]
result = ""

for chunk in client.send_message("chinchilla", message, with_chat_break=True):
  result += chunk["text_new"]

#delete the 3 latest messages, including the chat break
client.purge_conversation("capybara", count=3)

# Abrir un archivo para escritura
f = open("prueba.txt", "w")

# Escribir el resultado en el archivo
f.write(result)

# Cerrar el archivo
f.close()

print ("Tu consulta ha sido copiada")
