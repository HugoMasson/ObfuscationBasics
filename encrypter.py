import sys

"""
	Encrypter : simple code to encrypt / decrypt txt files

	Hugo Masson 27/08/2022

	Content :
		- Caesar cipher
"""

SHOW_LIST 	= False
PY_VER		= "Created on python 3.10.6"
VERSION 	= "1.0.0"
DATE		= "start 27/08/2022 last 28/08/2022"
USABLE  	= {
	"Caesar cipher run: 'python encrypter.py -[e/d] -caesar file.txt [password_int]' ":"https://en.wikipedia.org/wiki/Caesar_cipher",
	"Xor cipher run: 'python encrypter.py -[e/d] -xor file.txt' ":"https://en.wikipedia.org/wiki/XOR_cipher",
}

#to color the terminal :O
#from -> https://stackoverflow.com/questions/287871/how-do-i-print-colored-text-to-the-terminal
class bcolors:
    HEADER 		= '\033[95m'
    OKBLUE 		= '\033[94m'
    OKCYAN 		= '\033[96m'
    OKGREEN 	= '\033[92m'
    WARNING 	= '\033[93m'
    FAIL 		= '\033[91m'
    ENDC 		= '\033[0m'
    BOLD 		= '\033[1m'
    UNDERLINE 	= '\033[4m'

#just some headers
def startProgram():
	print("\n"+"#"*90+"\n")
	print(f"Encrypter {VERSION} -> {DATE} by {bcolors.BOLD}Hugo Masson {PY_VER}{bcolors.ENDC}\n")
	if SHOW_LIST:
		for key in USABLE:
			print(" "*5+f"{bcolors.OKCYAN}{key}{bcolors.ENDC}\n")
	print("  To get info on the method of encryption run 'python encrypter.py info [method_name]'\n")
	print("#"*90)
	print("\n")

#convert base 10 (decimal) into base 2 (binary) returned as list
def getBinaryFromASCII(asciiCode):
	q = asciiCode
	r = []
	while q != 0:
		r.append(q%2)
		q = q // 2
	
	#adding 0 to have 8 bits
	for i in range(8-len(r)):
		r.append(0)
	r.reverse()
	return r


def getFileAsString(path):
	with open(path, 'r') as file:
		data = file.read()
	return data

def overrideFile(path, content):
	with open(path, 'w') as file:
		file.write(content)
	print("New file content:\n"+content)

# working
def caesarCipher(arr, encrypt):
	text = getFileAsString(arr[0])
	key  = int(arr[1]) % encrypt
	cryptText = ""
	for letter in text:
		if letter != " " and letter != "\n":
			cryptText += chr(ord(letter) + key)
		else:
			cryptText += letter
	return cryptText

#not optimised at all just wanted to work with arrays
def xorCipherEncry(arr):
	if len(arr[1]) != 8:
		raise Exception("for Xor you have to use a 8 bit key e.g '01010101'")
	text = getFileAsString(arr[0])
	
	#get encoded file as 2d array of 8 bits
	enc = []
	for char in text:
		enc.append([])
		a = getBinaryFromASCII(ord(char))
		for i in range(len(a)):
			if int(a[i]) != int(arr[1][i]):
				enc[len(enc)-1].append(1)
			else:
				enc[len(enc)-1].append(0)
	
	output = ""
	for i in range(len(enc)):
		string = ""
		for j in range(len(enc[i])):
			string += str(enc[i][j])
		output += chr(int(string, 2))

	return output




def encypt(arr):
	v = arr[0]
	if v == "-caesar":
		overrideFile(arr[1], caesarCipher(arr[1:], 26))
	elif v == "-xor":
		overrideFile(arr[1], xorCipherEncry(arr[1:]))
	else:
		l = ""
		for key in USABLE:
			l += " "*5+f"{bcolors.OKCYAN}{key}{bcolors.ENDC}\n"
		raise Exception(f" is not an accepted algorithm name list of commands:\n{l}")
		

def decrypt(arr):
	v = arr[0]
	arr[2] = -int(arr[2])
	if v == "-caesar":
		overrideFile(arr[1], caesarCipher(arr[1:], -26))
	elif v == "-xor":
		overrideFile(arr[1],xorCipherEncry(arr[1:]))
	else:
		l = ""
		for key in USABLE:
			l += " "*5+f"{bcolors.OKCYAN}{key}{bcolors.ENDC}\n"
		raise Exception(f" is not an accepted algorithm name list of commands:\n{l}")








def main(arr):
	if arr[0] == "-e":
		encypt(arr[1:])
	elif arr[0] == "-d":
		decrypt(arr[1:])
	else:
		raise Exception("Sorry, the first argument has to be '-e' or '-d' (encrypt or decrypt) not "+arr[0])


if __name__ == '__main__':
	startProgram()
	if len(sys.argv) == 1:
		print(f"{bcolors.UNDERLINE}{bcolors.BOLD}{bcolors.FAIL}Error: you have to specify the arguments see the list below{bcolors.ENDC}{bcolors.ENDC}{bcolors.ENDC}\n\n")
		for key in USABLE:
			print(" "*5+f"{bcolors.OKCYAN}{key}{bcolors.ENDC}\n")
	else:	
		main(sys.argv[1:])

	print("\n")




