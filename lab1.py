import requests
response = requests.get('https://github.com/peijen/cmput404-Lab1/raw/master/lab1.py')
print(response.text)
