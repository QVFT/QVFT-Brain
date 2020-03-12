import requests, json

data = {'var_val':54,
        'env_var_id': 'Temperature',
        'shelf_id':1,
        'sensor_id':1,
        'arduino_id':1}

url = f"http://localhost:5000/api/readings/{data['env_var_id']}"

headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

r = requests.post(url, data=json.dumps(data), headers=headers)
print(r)