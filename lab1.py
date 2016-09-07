import requests
response = requests.post('http://ccid-eddieantonio.rhcloud.com/peijen')
print(response.status_code)
