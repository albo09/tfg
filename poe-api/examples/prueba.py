import poe
import logging
import sys

#send a message and immediately delete it

token = "1tGpkkmxDTZ6knsf-TA2yw%3D%3D"
poe.logger.setLevel(logging.INFO)
client = poe.Client(token)


message = sys.argv[1]
for chunk in client.send_message("chinchilla", message, with_chat_break=True):
  print(chunk["text_new"], end="", flush=True)

#delete the 3 latest messages, including the chat break
client.purge_conversation("capybara", count=3)
