def read_plaintext(filename):
	"reads plaintext from a file and returns it as a string"
	with open(filename, 'r') as file:
		return file.read()

def write_ciphertext(filename, ciphertext):
	"writes the ciphertext to a file"
	with open(filename, 'w') as file:
		file.write(ciphertext)

def read_ciphertext(filename):
	"reads ciphertext from a file and returns it as a string"
	with open(filename, 'r') as file:
		return file.read()
	
def write_plaintext(filename, plaintext):
	"writes the plaintext to a file"
	with open(filename, 'w') as file:
		file.write(plaintext)