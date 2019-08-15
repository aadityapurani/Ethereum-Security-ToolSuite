import requests
import sys

# Users should input contract along with 0x in the first parameter
contract_addr = sys.argv

latest="latest"
sess = requests.Session()

data = {"jsonrpc":"2.0","method":"eth_getCode","params":["0x0A3e0F6896294dE0a623469981914E599fC3b45F", "0x1"],"id":1}

URL = 'http://127.0.0.1:7545/'

for i in range(10000):
	data['params'][1] = hex(i)
	r = sess.post(URL, json=data)
	print r.json()
	if str(r.json()) == "{u'jsonrpc': u'2.0', u'id': 1, u'result': u'0x'}":
		print "Not Found"
	else:
		print r.json()
		print hex(i)
		break
