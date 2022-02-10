import requests

payload = {'FirstName': 'Gunalan', 'LastName': 'Deivaganapathy'}
r = requests.get('https://httpbin.org/get', params=payload) # params is a dictionary of key-value pairs which is used while using GET method

print(r.content)
print("get",r.text) # will return decoded text

pos = requests.post('https://httpbin.org/post', data=payload) # data will be used with POST method
print("post",pos.text)