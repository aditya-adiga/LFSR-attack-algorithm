# Known plaintext attack against LFSRs.
import numpy as np


def createdict():
	alphadict={}
	alphabet='abcdefghijklmnopqrstuvwxyz'
	for i in range(26):
		alphadict[alphabet[i]]=i
	for i in range(6):
		alphadict[str(i)]=i+26
	return alphadict

def reversedict(alphadict):
	numdict={v:k for k,v in alphadict.items()}

def convert_to_binary(n):
	return bin(n).replace("0b", "").zfill(5)
def convert_text_to_binary(plain_text,alphadict):
	binary_text=''
	for i in plain_text:
		binary_text+=convert_to_binary(alphadict[i])
	return binary_text
def calculate_key_stream(plain_binary,encrypted_binary):
	key=''
	for i in range(len(plain_binary)):
		key+=str((int(plain_binary[i])+int(encrypted_binary[i]))%2)
	return key
def lfsr_generator(key,period):
	res=[]
	array=[]
	for i in range(period):
		res.append(key[i+6])
		array.append(key[i:i+6])
	res1=np.array(res)
	arr1=np.array(array)
	print(arr1)
	print(res1)
	#key=binary_matrix_solver(arr1,res1)
	#return key
#def binary_matrix_solver(arr1,res1):
period=int(input('enter the period of LFSR'))
plain_text=input('enter the plain text available in the header information of the file')
encrypted_text=input('enter the encrypted text')
alphadict=createdict()
reversedict=reversedict(alphadict)
plain_binary=convert_text_to_binary(plain_text,alphadict)
encrypted_binary=convert_text_to_binary(encrypted_text,alphadict)
key=calculate_key_stream(plain_binary,encrypted_binary)
lfsr_generator(key,period)



