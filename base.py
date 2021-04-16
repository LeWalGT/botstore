import base64

#message = "Python is fun"

def enc(message):

	message_bytes = message.encode('ascii')
	base64_bytes = base64.b64encode(message_bytes)
	base64_message = base64_bytes.decode('ascii')
	return base64_message

	#print(base64_message)

#leo = enc(message)
#print(leo)

def dec(message):
	base64_bytes = message.decode('ascii') #encode
	message_bytes = base64.b64decode(base64_bytes)
	messages = message_bytes.decode('ascii')
	return messages


def decc(message):
	base64_bytes = message.encode('ascii')
	message_bytes = base64.b64decode(base64_bytes)
	messages = message_bytes.decode('ascii')
	return messages

#print(enc('NzY4MzA3NTkxNTIzNTk4MzU2.X4-kNA.PjPCVj7dX6wTI1-P_gsdbLvhy0k'))
#print(decc("TnpZNE16QTNOVGt4TlRJek5UazRNelUyLlg0LWtOQS5QalBDVmo3ZFg2d1RJMS1QX2dzZGJMdmh5MGs="))

#leo2 = dec(leo)
#print(leo2)