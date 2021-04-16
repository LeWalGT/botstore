import base64

def enc(message):

	message_bytes = message.encode('ascii')
	base64_bytes = base64.b64encode(message_bytes)
	base64_message = base64_bytes.decode('ascii')
	return base64_message


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

