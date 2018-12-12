import json
import requests
url='http://free.currencyconverterapi.com/api/v5/convert?q=USD_INR&compact=y'
response=requests.get(url)
python_dict=response.json()
user_input=int(input("Enter the value of INR: "))
#print(python_dict)
result_value=user_input/python_dict['USD_INR']['val']
print(result_value)
