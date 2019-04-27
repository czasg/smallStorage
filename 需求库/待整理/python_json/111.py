import json

data = [ { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 } ]

#dumps
"""
with open('cza.json', 'w') as f_w:
	json_data = json.dumps(data)
	print(json_data)
	f_w.write(json_data)
"""

#loads
"""
with open('cza.json', 'r') as f_r:
	json_data = json.loads(f_r.read())
	print(json_data)
	print(type(json_data))
	print(isinstance(json_data, bytes))
	print(isinstance(json_data, str))
"""	

#json_data = json.dumps(data)
#print(type(json_data))
#print(isinstance(json_data, bytes))
#print(isinstance(json_data, str))