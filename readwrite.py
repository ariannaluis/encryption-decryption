def read_plaintext(filename):
	with open(filename, 'r') as file:
		return file.read()

def write_ciphertext(filename, ciphertext):
	with open(filename, 'w') as file:
		file.write(ciphertext)

def read_ciphertext(filename):
	with open(filename, 'r') as file:
		return file.read()
	
def write_plaintext(filename, plaintext):
	with open(filename, 'w') as file:
		file.write(plaintext)