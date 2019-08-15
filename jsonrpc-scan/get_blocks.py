import requests

sess = requests.Session()
data = {"jsonrpc":"2.0","method":"eth_getBlockByNumber","params":["0x1", True],"id":1}
URL = 'http://localhost:7545/'
for i in range(10000):
	data['params'][0] = hex(i)
	r = sess.post(URL, json=data)
	print r.json()
