import requests, json

# data = {'var_val':54,
#         'env_var_id': 'Temperature',
#         'shelf_id':1,
# #        'sensor_id':1,
# #         'arduino_id':1}

url = f"http://localhost:5000/api/readings/Temperature?start_time=1583532012&end_time=1584050412"

headers = {'Accept': 'text/plain'}

r = requests.get(url=url, headers=headers)
print(r)
print(r.text)